# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-26 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_bbs_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs_user',
            name='username',
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default='/static/images/user.png', upload_to='/static/images/'),
        ),
    ]
