# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-16 05:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0012_auto_20160712_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 16, 5, 56, 58, 261144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 16, 5, 56, 58, 261144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 16, 5, 56, 58, 269150, tzinfo=utc)),
        ),
    ]
