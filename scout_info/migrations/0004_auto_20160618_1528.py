# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 08:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scout_info', '0003_auto_20160618_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 6, 18, 8, 28, 7, 730214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 6, 18, 8, 28, 7, 730214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scout_profile',
            name='position',
            field=models.CharField(choices=[('NON', 'Không có'), ('SPL', 'Đội trưởng Nhất'), ('ASPL', 'Phụ tá Đội trưởng Nhất'), ('ATL', 'Thiếu phó/Phụ tá'), ('PL', 'Thiếu trưởng'), ('STL', 'Liên đoàn Trưởng')], max_length=4, null=True),
        ),
    ]
