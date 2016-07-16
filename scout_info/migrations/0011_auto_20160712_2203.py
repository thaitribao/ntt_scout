# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 15:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0010_auto_20160712_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 12, 15, 3, 46, 274307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to='team_management.Member'),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 12, 15, 3, 46, 274307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scout_info.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 12, 15, 3, 46, 282331, tzinfo=utc)),
        ),
    ]