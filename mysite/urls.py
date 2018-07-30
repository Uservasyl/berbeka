from django.conf.urls import url, include
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^contact/$', views.contact, name='contact'),
]
