from django.conf.urls import url, include, patterns
from django.contrib import admin
from .views import page, login_user, logout_user
# from persons import views as person_views

urlpatterns = patterns('',

    url(r'^persons/', include('persons.urls', namespace='persons')),
    url(r'^login/$', login_user),
    url(r'^logout/$', logout_user),
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),
#    url(r'^admin/', include(admin.site.urls)),
    # url(r'^persons/$', person_views.persons, name='persons'),  
    # url(r'^persons/add/$', person_views.add_person, name='add_person'),
)
