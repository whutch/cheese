# -*- coding: utf-8 -*-
"""Admin models and registration for core app."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)

from django.contrib import admin

from . import models


admin.site.register(models.UserData)
