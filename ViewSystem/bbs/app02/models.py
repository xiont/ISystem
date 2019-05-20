from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Oday(models.Model):
    title = models.CharField(max_length=128,unique= True)
    time = models.DateField()
    link = models.URLField()

class Bobao360(models.Model):
    title = models.CharField(max_length=128,unique= True)
    time = models.DateField()
    link = models.URLField()
    source = models.CharField(max_length=128)

class Security_event(models.Model):
    event_title = models.CharField(max_length=128,unique= True)
    event_time = models.DateField()
    event_url = models.URLField()
    event_platform = models.CharField(max_length=128,default="")

class Bug(models.Model):
    bug_name = models.CharField(max_length=128,unique= True)
    bug_id = models.CharField(max_length=128,default="")
    bug_time = models.DateField()
    bug_url = models.URLField()
    bug_platform = models.CharField(max_length=128,default="")
    bug_type = models.CharField(max_length=128,default="")