# -*- coding: utf-8 -*-
"""URL configuration for core app."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns("",
    url(r"^$", views.home, name="site_home"),
)
