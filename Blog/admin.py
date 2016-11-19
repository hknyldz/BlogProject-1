# -*- coding: utf-8 -*-
from django.contrib import admin
from Blog.models import Post,Content_media,Category
# Register your models here.


class MediaInline(admin.TabularInline):
    model = Content_media
    extra = 0

class Blog(admin.ModelAdmin):
    exclude = ('seo_url',)
    list_display = ('title','seo_url','time','category_list','is_active')
    search_fields = ('title', 'content','is_active')
    list_editable = ('category_list', 'is_active','time')
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
    )
    inlines = [MediaInline]

class Admin_category(admin.ModelAdmin):
    exclude = ('seo_url',)
admin.site.register(Post,Blog)
admin.site.register(Content_media)
admin.site.register(Category,Admin_category)