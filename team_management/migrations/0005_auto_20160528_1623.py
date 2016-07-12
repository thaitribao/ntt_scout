# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 09:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0004_auto_20160528_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 28, 9, 23, 38, 245410, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 5, 28, 9, 23, 38, 234902, tzinfo=utc)),
        ),
    ]