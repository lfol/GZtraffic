# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='road_base_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amap_id', models.CharField(max_length=10)),
                ('amap_ids', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=30)),
                ('shapes', models.TextField()),
            ],
        ),
    ]