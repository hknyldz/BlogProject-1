# sitemaps.py
from django.contrib import sitemaps
from .models import post,category

url_list = []
def sitemap_db():
    # post ve category urlleri aliyorum.
    post_db = post.objects.all()
    for i in post_db:
        url_list.append('/' + i.seo_url)
    category_db = category.objects.all()
    for i in category_db:
        url_list.append('/kategori/' + i.seo_url)
    return url_list

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['','/hakkimda','/iletisim']+sitemap_db()

    def location(self, item):
        return item