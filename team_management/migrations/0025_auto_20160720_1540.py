# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0024_auto_20160719_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 8, 40, 11, 94061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 8, 40, 11, 91556, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 8, 40, 11, 92060, tzinfo=utc)),
        ),
    ]
