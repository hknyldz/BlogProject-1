from django.shortcuts import render
from Blog.models import post
# Create your views here.
def home(request):
    return render(request,'profil.html',locals())

def about(request):
    return render(request,'about.html',locals())

def contact(request):
    return render(request,'contact.html',locals())

def blog(request):
    db = post.objects.all()
    return render(request,'blog.html',locals())