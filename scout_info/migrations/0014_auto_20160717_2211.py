# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-17 15:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0013_auto_20160716_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 17, 15, 11, 51, 905218, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 17, 15, 11, 51, 905218, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 17, 15, 11, 51, 913219, tzinfo=utc)),
        ),
    ]
