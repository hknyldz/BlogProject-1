from Blog.models import post
url_list = []
db = post.objects.all()
for i in db:
    url_list.append("/makale/"+i.seo_url)
# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['','/hakkimda','/blog','/iletisim']+url_list

    def location(self, item):
        return item