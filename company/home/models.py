from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.context_processors import static


class Product(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name


class Slider(models.Model):
    # name = models.CharField(max_length=200)
    img = models.ImageField(upload_to=' public/images/sliders')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    # cover = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def url(self, short=False):
        if short is False:
            return static + self.img.url[7:]
        return self.img.url[7:]

    def show_img(self):
        from django.utils.html import mark_safe
        return mark_safe('<img width="100" src= "slide_01.jpg"' + self.url())

class Blog(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    view = models.IntegerField(default=0)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True)
    title = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employment(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Massage(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    mail = models.CharField(max_length=50)
    tel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
