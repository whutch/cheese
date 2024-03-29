# -*- coding: utf-8 -*-
"""View functions for core app."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)

from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")
