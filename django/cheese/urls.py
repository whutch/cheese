# -*- coding: utf-8 -*-
"""Base URL configuration."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)

from django.conf.urls import include, url
from django.contrib import admin

from .apps.core import urls as core_urls


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^", include(core_urls)),
]
