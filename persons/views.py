import sys, os

from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from persons.models import Person
from persons.forms import addPersonForm, searchPersonForm

from simple.settings import *
import simple



def index_persons(request):

    personsList = Person.objects.all().order_by('id')
    #print ' **** PERSONSLIST ****: ', personsList

    """Render the requested page if found."""
    page = simple.views.get_page_or_404( os.path.join(SITE_PAGES_DIRECTORY, 'persons.html') )
    context = {
        'personsList': personsList,
        'page': page,
    }

    return render(request, 'page.html', context)
    #return simple.views.page(request, 'persons')

def search_person(request):


    if 'q' not in request.GET:
        return HttpResponse("Invalid GET request")

    personsList = Person.objects.all().order_by('id')
    page = simple.views.get_page_or_404( os.path.join(SITE_PAGES_DIRECTORY, 'persons.html') )
    context = {
            'personsList': personsList,
            'page': page,
    }

    if request.GET['q']:
        q = request.GET['q']
        persons = Person.objects.filter(username__icontains= q)
        if len(persons) > 0:
            context['personsListResult'] = persons
        else:
            context['message'] = 'None Found'
    else:
        context['message'] = 'Error in submission'

    return render(request, 'page.html', context)


def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

@login_required
def add_person(request):
    #print '**** ADDING PERSON ****'

    if request.user.is_authenticated():

        if request.method == 'GET':
            form = addPersonForm(request.POST)
            page = simple.views.get_page_or_404( os.path.join(SITE_PAGES_DIRECTORY, 'add_person.html') )

            context = RequestContext (request, { 
                'form' : form,
                'page' : page
            }, [ip_address_processor])

            return render_to_response('page.html', context)

        else:

            form = addPersonForm(request.POST)
            if form.is_valid():
                #print 'Valid form'
                newPerson = form.save()
                #newPerson.save()  #redudant. Usefull if form.save(commit=False)

            else:
                #print form
                print 'INVALID FORM DATA'

            return HttpResponseRedirect('/persons/')
    else:
        print 'Need to login first'
        return HttpResponseRedirect('/login')

