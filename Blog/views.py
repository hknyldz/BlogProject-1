# -*- coding: utf-8 -*-
from django.shortcuts import render,get_list_or_404
from Blog.models import Post, Category
from django.core.paginator  import Paginator,EmptyPage
from django.http import Http404,HttpResponse
from BlogProject.settings import web_site_name,web_site_slogan,web_site_url
from django.db.utils import OperationalError
# Create your views here.
def home(request):
    """Ana Sayfa"""
    db = Post.objects.filter(is_active=True).order_by('?')[:6]
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'home.html', {
        'db': db,
        'last_db':last_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def about(request):
    """ Hakkimda Sayfasi """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'about.html', {
        'last_db': last_db,
        'web_site_name':web_site_name,
        'web_site_slogan':web_site_slogan,
    })


def contact(request):
    """ iletisim sayfasi """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request, 'contact.html', {
        'last_db': last_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def blog(request):
    """ blog yazilarin listelendigi yer ve ana sayfa"""
    try:
        last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
        db = Post.objects.filter(is_active=True).order_by('-time')[:6]
        post_db = Post.objects.filter(is_active=True)
        category_db = Category.objects.all()
        pages = Paginator(post_db, 5)
        return render(request, 'blog.html', {
            'last_db': last_db,
            'db': db,
            'pages': pages,
            'category_db': category_db,
            'web_site_name': web_site_name,
            'web_site_slogan': web_site_slogan,
        })
    except OperationalError:
        return HttpResponse('<b><center>Merhaba, büyük ihtimal bu projeyi yeni kurdun.<br></b>'
                            'Lütfen veritabanı yapılandırılması yap. <br> python manage.py makemigrations'
                            '<br> python manage.py migrate </center>')

def page(request,id):
    """ Blog Sayfalamasi """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    post_db = Post.objects.filter(is_active=True).order_by('-time')
    category_db = Category.objects.all()
    pages = Paginator(post_db,5)
    try:
        db = pages.page(id)
    except EmptyPage:
        raise Http404()
    return render(request, 'page.html', {
        'last_db': last_db,
        'db': db,
        'pages': pages,
        'category_db': category_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def blog_details(request, slug):
    """ makale_details sayfasi """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db = Category.objects.all()
    db = Post.objects.filter(seo_url=slug,is_active=True)
    for seo_info in db:
        title = seo_info.title
        description = seo_info.description
        keywords = seo_info.keywords
        image =  seo_info.image
    return render(request, 'blog_details.html', {
        'last_db': last_db,
        'db': get_list_or_404(db),
        'category_db': category_db,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan,
        'web_site_url':web_site_url,
        'title':title,
        'description':description,
        'keywords':keywords,
        'image':image
    })


def category_view(request, category_names):
    """ category details sayfasi """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db_list = Category.objects.all()
    category_db = Category.objects.filter(seo_url=category_names)
    post_db = Post.objects.filter(category_list__seo_url=category_names,is_active=True).order_by('-time')
    pages = Paginator(post_db,5)
    for seo_info in category_db:
        title = seo_info.category_name
        description = seo_info.category_description
        keywords = seo_info.category_keywords
    return render(request, 'category.html', {
        'last_db': last_db,
        'category_db_list': category_db_list,
        'category_db': category_db,
        'post_db': post_db,
        'pages':pages,
        'category_names':category_names,
        'title': title,
        'description': description,
        'keywords': keywords,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })



def category_page(request, category_names,id):
    """ category details sayfası """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    category_db_list = Category.objects.all()
    category_db = Category.objects.filter(seo_url=category_names)
    post_db = Post.objects.filter(category_list__seo_url=category_names,is_active=True).order_by('-time')
    pages = Paginator(post_db,5)
    for seo_info in category_db:
        title = seo_info.category_name
        description = seo_info.category_description
        keywords = seo_info.category_keywords
    try:
        db = pages.page(id)
    except EmptyPage:
        raise Http404()
    return render(request, 'category_page.html', {
        'last_db': last_db,
        'category_db_list': category_db_list,
        'category_db': category_db,
        'post_db': db,
        'pages':pages,
        'category_names':category_names,
        'title': title,
        'description': description,
        'keywords': keywords,
        'web_site_name': web_site_name,
        'web_site_slogan': web_site_slogan
    })


def human(request):
    """ humans.txt"""

    return render(request, 'blog_templates/humans.html')


def robots(request):
    """robots.txt"""

    return render(request, 'blog_templates/robots.html')

def last_content(request):
    """ Alt taraf son yazılar """
    last_db = Post.objects.filter(is_active=True).order_by('-time')[:3]
    return render(request,'blog_templates/last_content.html',{
        'last_db':last_db
    })
