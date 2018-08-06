# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from AMapReader.models import road_base_info
# Register your models here.
from django_object_actions import DjangoObjectActions


@admin.register(road_base_info)
class UserAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('id', 'name', 'location')

    list_editable = ('name',)

    # 定制Action行为具体方法
    def func(self, request, queryset):
        print(self, request, queryset)
        print(request.POST.getlist('_selected_action'))

    func.short_description = "中文显示自定义Actions"
    actions = [func, ]

    # Action选项都是在页面上方显示
    actions_on_top = True
    # Action选项都是在页面下方显示
    actions_on_bottom = False

    # 是否显示选择个数
    actions_selection_counter = True

    def view_on_site(self, obj):
        return 'https://ditu.amap.com/place/%s' % obj.amap_id

    def publish_this(self, request, obj):
        return 'https://ditu.amap.com/place/%s' % obj.amap_id

    publish_this.label = "Publish"  # optional
    publish_this.short_description = "Submit this article"  # optional

    change_actions = ('publish_this',)
