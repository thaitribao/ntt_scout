# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 04:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team_management', '0010_auto_20160606_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('start_date', models.DateField(default=datetime.datetime(2016, 6, 6, 4, 4, 35, 974039, tzinfo=utc))),
                ('end_date', models.DateField(default=datetime.datetime(2016, 6, 6, 4, 4, 35, 974039, tzinfo=utc))),
                ('comment', models.TextField(max_length=1000, null=True)),
                ('members', models.ManyToManyField(to='team_management.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Scout_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('khan_quang', models.BooleanField(default=False)),
                ('tan_sinh', models.BooleanField(default=False)),
                ('hang_nhi', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[('SPL', 'Senior Patrol Leader'), ('ASPL', 'Assistant Senior Patrol Leader'), ('ATL', 'Assistant Troop Leader'), ('PL', 'Troop Leader'), ('STL', 'Super Troop Leader')], max_length=4, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team_management.Member')),
            ],
        ),
    ]