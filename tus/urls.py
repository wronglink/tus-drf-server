# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from tus.views import home, files_root, FileUploadView

urlpatterns = patterns('',
    url(r'^$', home,  name='home'),
    url(r'^files/$', files_root, name='files-root'),
    url(r'^files/(?P<filename>[a-zA-Z0-9]+)/$', FileUploadView.as_view(), name='file-upload'),
)
