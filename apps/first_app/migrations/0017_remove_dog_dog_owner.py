# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0016_dog_dog_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='dog_owner',
        ),
    ]
