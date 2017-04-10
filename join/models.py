# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Join(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True,auto_now = False)
	updated = models.DateTimeField(auto_now_add = False,auto_now = True)


def __str__(self):
	return str(self.email)

def __unicode__(self):
	return str(self.email)



# Create your models here.
