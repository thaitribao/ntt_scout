# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-05 09:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0006_auto_20160705_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 5, 9, 5, 47, 64037, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 5, 9, 5, 47, 63537, tzinfo=utc)),
        ),
    ]
