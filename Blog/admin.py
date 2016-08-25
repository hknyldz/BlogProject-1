from django.contrib import admin
from Blog.models import post,content_media,category
# Register your models here.


class MediaInline(admin.TabularInline):
    model = content_media
    extra = 0

class Blog(admin.ModelAdmin):
    list_display = ('title', 'content', 'keywords', 'description', 'image','time','category_list')
    search_fields = ('title', 'content')
    inlines = [MediaInline]

admin.site.register(post,Blog)
admin.site.register(content_media)
admin.site.register(category)