# sitemaps.py
from django.contrib import sitemaps
from .models import Post,Category

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def sitemap_db(self):
        # post ve category urlleri aliyorum.
        try:
            url_list = []
            post_db = Post.objects.all()
            for i in post_db:
                url_list.append('/' + i.seo_url)
            category_db = Category.objects.all()
            for i in category_db:
                url_list.append('/kategori/' + i.seo_url)
            return url_list
        except:
            url_list = []
            return url_list

    def items(self):
        return ['','/hakkimda','/iletisim','/anasayfa']+self.sitemap_db()

    def location(self, item):
        return item