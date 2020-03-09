# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0012_dog_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ManyToManyField(related_name='likes', to='first_app.Dog')),
            ],
        ),
    ]