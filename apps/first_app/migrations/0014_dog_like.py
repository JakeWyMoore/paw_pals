# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_remove_dog_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='like',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
