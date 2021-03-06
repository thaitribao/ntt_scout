# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-20 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0016_auto_20160720_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 846616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 846616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 15, 18, 2, 856124, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scout_profile',
            name='hang_nhi_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 15, 18, 2, 843614, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='scout_profile',
            name='khan_quang_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 15, 18, 2, 843137, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='scout_profile',
            name='tan_sinh_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 7, 20, 15, 18, 2, 843614, tzinfo=utc), null=True),
        ),
    ]
