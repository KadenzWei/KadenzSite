from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SheetList(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True)
    instrument = models.CharField(max_length=100,blank=True)
    source = models.CharField(max_length=100,blank=True)
    link = models.URLField(blank=True) #youtube piano video
    picture = models.URLField(blank=True)
    describe = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    difficulty = models.DecimalField(max_digits=1,decimal_places=0,blank=True)
    page = models.DecimalField(max_digits=2,decimal_places=0,blank=True)
    tag = models.TextField(blank=True)
    isPublic = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
