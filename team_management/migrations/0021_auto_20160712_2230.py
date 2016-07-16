# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0020_auto_20160712_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 12, 15, 30, 55, 523318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 7, 12, 15, 30, 55, 520310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_school',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='dad_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='health_info',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 12, 15, 30, 55, 520310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='mom_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]