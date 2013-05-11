# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from tus.views import FileUploadView, home

urlpatterns = patterns('',
    url(r'^$', home,  name='home'),
    url(r'^files/(?P<filename>[a-zA-Z0-9]+)/$', FileUploadView.as_view(), name='file-upload'),
)
