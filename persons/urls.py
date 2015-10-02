from django.conf.urls import patterns, url
#from persons.views import index_persons, add_person
from persons import views

#views.index_persons('GET / HTTP/1.0')
#print 'AFGRGWRGWEGFWJNEIFWJEF'   #INCLUDED

urlpatterns = patterns('',
    url(r'^$', views.index_persons, name='index_persons'),  
    url(r'^add/', views.add_person, name='add_person'),
    url(r'^search/', views.search_person, name='search_person'),
)