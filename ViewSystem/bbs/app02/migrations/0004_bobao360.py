# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0003_auto_20170304_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bobao360',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('time', models.CharField(max_length=128)),
                ('link', models.URLField()),
                ('source', models.CharField(max_length=128)),
            ],
        ),
    ]
