# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-01 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20171030_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]