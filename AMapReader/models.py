# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class road_base_info(models.Model):
    amap_id = models.CharField(max_length=10, null=True, blank=True)
    amap_ids = models.CharField(max_length=200, null=True, blank=True)  # 备选ID
    name = models.CharField(max_length=100)  # 路名
    location = models.CharField(max_length=30, null=True, blank=True)  # 经纬度坐标（点）
    shapes = models.TextField(null=True, blank=True)  # AMap shape图形
