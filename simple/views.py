import json
import os

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context, RequestContext
from django.template.loader_tags import BlockNode
from django.utils._os import safe_join
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
        #print file_path
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def page(request, slug='index'):
    print 'PAGE view function'

    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }

    return render(request, 'page.html', context)


def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print username, password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                print 'logging in ', user
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect('/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    context = RequestContext (request, {'state':state, 'username': username}, [ip_address_processor])
    return render_to_response('auth.html', context)

def logout_user(request):
    logout(request)
    return page(request, slug='index')

