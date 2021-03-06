# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-01 09:26
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0008_auto_20160531_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 9, 26, 6, 181666, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 9, 26, 6, 186675, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 6, 1, 9, 26, 6, 180665, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_grade',
            field=models.PositiveIntegerField(default=6, validators=[django.core.validators.MaxValueValidator(13), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_school',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='health_info',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
