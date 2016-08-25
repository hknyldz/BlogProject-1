from django.shortcuts import render
from Blog.models import post,category
# Create your views here.
def home(request):
    """Ana Sayfa"""
    db = post.objects.order_by('?')[:6]
    return render(request,'profil.html',{
        'db':db
    })

def about(request):
    """ Hakkımda Sayfası """
    last_db = post.objects.order_by('?')[:3]
    return render(request,'about.html',{
        'last_db':last_db
    })

def contact(request):
    """ İletişim Sayfası """
    last_db = post.objects.order_by('?')[:3]
    return render(request,'contact.html',{
        'last_db': last_db
    })

def blog(request):
    """ Blog yazıların listelendiği sayfa"""
    last_db = post.objects.order_by('?')[:3]
    db = post.objects.all()
    category_db = category.objects.all()
    return render(request,'blog.html',{
        'last_db': last_db,
        'db':db,
        'category_db':category_db
    })

def makale(request,slug):
    """ makale_details sayfası """
    last_db = post.objects.order_by('?')[:3]
    category_db = category.objects.all()
    db = post.objects.filter(seo_url=slug)
    return render(request,'blog_details.html',{
        'last_db': last_db,
        'db':db,
        'category_db':category_db
    })
def category_view(request,category_names):
    """ category details sayfası """
    last_db = post.objects.order_by('?')[:3]
    category_db_list = category.objects.all()
    category_db = category.objects.filter(category_name=str(category_names))
    post_db = post.objects.filter(category_list__category_name=category_names)
    return render(request,'category.html',{
        'last_db': last_db,
        'category_db_list':category_db_list,
        'category_db':category_db,
        'post_db':post_db
    })

def human(request):
    """ humans.txt"""
    return render(request,'humans.html')
def robots(request):
    """robots.txt"""
    return render(request,'robots.html')