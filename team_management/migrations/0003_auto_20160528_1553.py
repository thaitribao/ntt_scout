# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0002_auto_20160528_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 28, 8, 53, 0, 562918, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 5, 28, 8, 53, 0, 560978, tzinfo=utc)),
        ),
    ]