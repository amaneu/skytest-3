# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^node-contents', 'browser.views.node_contents'),

    url(r'^$', 'browser.views.index'),
    url(r'^/$', 'browser.views.index'),

)
