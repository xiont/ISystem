# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20170117_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='sign',
            field=models.CharField(default='\u5176\u4ed6', max_length=64),
        ),
    ]
