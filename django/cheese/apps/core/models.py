# -*- coding: utf-8 -*-
"""Data models for core app."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)

from django.contrib.auth.models import User
from django.db import models


class UserData(models.Model):
    user = models.ForeignKey(User, unique=True)

    class Meta:
        ordering = ("user",)

    def __str__(self):
        return str(self.user)
