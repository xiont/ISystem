#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    sign = models.CharField(max_length=64,default='其他')
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy.')
    photo = models.ImageField(upload_to="/static/images/",default="static/images/user.png")

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = BBS_user()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
