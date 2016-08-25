from django.shortcuts import render
from Blog.models import post,category
# Create your views here.
def home(request):
    return render(request,'profil.html',locals())

def about(request):
    return render(request,'about.html',locals())

def contact(request):
    return render(request,'contact.html',locals())

def blog(request):
    db = post.objects.all()
    category_db = category.objects.all()
    return render(request,'blog.html',locals())

def makale(request,slug):
    category_db = category.objects.all()
    db = post.objects.filter(seo_url=slug)
    return render(request,'blog_details.html',locals())

def category_view(request,category_names):
    category_db_list = category.objects.all()
    category_db = category.objects.filter(category_name=str(category_names))
    post_db = post.objects.filter(category_list__category_name=category_names)
    return render(request,'category.html',locals())