# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-05 09:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0015_auto_20160705_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 9, 5, 47, 58030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 7, 5, 9, 5, 47, 55529, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 5, 9, 5, 47, 56029, tzinfo=utc)),
        ),
    ]