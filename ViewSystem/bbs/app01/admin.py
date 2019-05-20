#encoding:utf-8
from django.contrib import admin
from app01 import models

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import BBS_user
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display =('title','summary','author','view_count','created_at')
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username')

admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)



class ProfileInline(admin.StackedInline):
    model = BBS_user
    max_num = 1
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)