# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AMapReader', '0003_auto_20180806_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road_base_info',
            name='amap_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='road_base_info',
            name='amap_ids',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='road_base_info',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='road_base_info',
            name='shapes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
