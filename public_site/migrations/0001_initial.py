# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, unique=True)),
                ('lyric', models.TextField(default='', max_length=2000)),
                ('link', models.URLField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]