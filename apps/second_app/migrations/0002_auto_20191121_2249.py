# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_remove_dog_like'),
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.ManyToManyField(related_name='like', to='first_app.Dog')),
            ],
        ),
        migrations.RemoveField(
            model_name='likes',
            name='like',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
