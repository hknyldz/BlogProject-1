"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from Blog.views import home,about,contact,blog,makale,category_view,human,robots

from Blog.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^hakkimda/', about, name='about'),
    url(r'^iletisim/', contact, name='contact'),
    url(r'^blog/', blog, name='blog'),
    url(r'^kategori/(?P<category_names>\w+)/$', category_view, name='category_view'),
    url(r'^makale/(?P<slug>[\w-]+)/$', makale, name='makale'),
    url(r'^humans.txt$', human, name='human'),
    url(r'^robots.txt$', robots, name='human'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
]