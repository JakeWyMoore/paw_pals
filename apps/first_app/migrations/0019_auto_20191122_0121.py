# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 01:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0018_auto_20191122_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='password',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='username',
        ),
    ]
