from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Slider(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True)
    alt = models.CharField(null=True, max_length=200)
    cover = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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




