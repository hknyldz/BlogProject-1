from Blog.models import post,category
url_list = []
post_db = post.objects.all()
for i in post_db:
    url_list.append('/'+i.seo_url)
category_db = category.objects.all()
for i in category_db:
    url_list.append('/kategori/'+i.seo_url)
# sitemaps.py
from django.contrib import sitemaps

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['','/hakkimda','/iletisim']+url_list

    def location(self, item):
        return item