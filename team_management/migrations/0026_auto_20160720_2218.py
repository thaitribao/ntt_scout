# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0025_auto_20160720_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 838634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 835609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 836107, tzinfo=utc)),
        ),
    ]
