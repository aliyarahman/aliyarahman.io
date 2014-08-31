from django.conf.urls import patterns, include, url
from seveneightten import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
)
