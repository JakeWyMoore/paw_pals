# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-22 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0021_auto_20191122_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='dog_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_dogs', to='first_app.User'),
        ),
    ]