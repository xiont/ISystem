# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20170226_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oday',
            name='time',
            field=models.DateField(),
        ),
    ]
