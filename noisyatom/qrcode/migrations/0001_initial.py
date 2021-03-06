# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(height_field=250, max_length=50, upload_to='', width_field=250)),
                ('is_active', models.BooleanField(default=True)),
                ('trigger', models.DateTimeField()),
                ('primary_url', models.URLField()),
                ('secondary_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'QRCodes',
                'verbose_name_plural': 'QRCode',
                'ordering': ['-created_at'],
            },
        ),
    ]
