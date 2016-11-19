# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from uuslug import slugify
from ajaximage.fields import AjaxImageField
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=500,null=True,unique=True)
    category_keywords = models.CharField(max_length=500,null=True)
    category_description = models.CharField(max_length=500,null=True)
    category_icon = models.CharField(max_length=100,null=True,verbose_name='Category Icon(fa-fa icon)')
    seo_url = models.CharField(max_length=500,null=True, blank=True,verbose_name='Seo_URL : (Otomatik doldurur)')
    class Meta:
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return '{}'.format(self.category_name)

    def save(self, *args, **kwargs):
        self.seo_url = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=500,null=True,unique=True)
    time = models.DateTimeField(auto_now=False,null=True)
    content = RichTextField(null=True)
    keywords = models.CharField(max_length=500,null=True)
    description = models.CharField(max_length=500,null=True)
    image = AjaxImageField(upload_to='blog_img')
    category_list = models.ForeignKey(Category,null=True)
    seo_url = models.CharField(max_length=500, null=True, blank=True,verbose_name='Seo_URL : (Otomatik doldurur)')
    is_active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Blog Yaz"

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.seo_url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Content_media(models.Model):
    blog = models.ForeignKey(Post)
    image = AjaxImageField(upload_to='blog_img')
    class Meta:
        verbose_name_plural = "Resim Ekle"

    def __str__(self):
        return '{}'.format(self.blog.title)

