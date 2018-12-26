from django.conf.urls import patterns, url

from data_mining import views

urlpatterns = patterns('',
    url(r'^myurl?claName=IN718', 'views.allmaterial'),
)
