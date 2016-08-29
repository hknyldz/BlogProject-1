from django.contrib import admin
from Blog.models import post,content_media,category
# Register your models here.


class MediaInline(admin.TabularInline):
    model = content_media
    extra = 0

class Blog(admin.ModelAdmin):
    list_display = ('title','seo_url','time','category_list','is_active')
    search_fields = ('title', 'content','is_active')
    list_editable = ('category_list', 'is_active','time')
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
    )
    inlines = [MediaInline]
admin.site.register(post,Blog)
admin.site.register(content_media)
admin.site.register(category)