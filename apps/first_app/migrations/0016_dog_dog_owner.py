# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_auto_20191121_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='dog_owner',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='dog_owner', to='first_app.User'),
            preserve_default=False,
        ),
    ]