# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class send(models.Model):
    message = models.CharField(max_length=2000)
    sender = models.CharField(max_length=100)

    def __str__(self):
        return self.message


class feed(models.Model):
    inputs = models.CharField(max_length=150)

    def __str__(self):
        return self.inputs
