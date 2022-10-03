from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
     
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=True,null=False)
    image = models.ImageField(upload_to='img/',blank=False,default=True)
    fon_image = models.ImageField(default=True,null=False,upload_to='img/')
    title_description = models.TextField(default=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title 

class First(models.Model):
     
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=True,null=False)
    image = models.ImageField(upload_to='img/',blank=False,default=True)
    fon_image = models.ImageField(default=True,null=False,upload_to='img/')
    title_description = models.TextField(default=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title 
