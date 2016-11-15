from django.contrib import admin
from Blog.models import post,content_media,category
# Register your models here.


class MediaInline(admin.TabularInline):
    model = content_media
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

class admin_category(admin.ModelAdmin):
    exclude = ('seo_url',)
admin.site.register(post,Blog)
admin.site.register(content_media)
admin.site.register(category,admin_category)