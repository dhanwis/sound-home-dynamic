from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='admin_app/products')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
class Project(models.Model):
    image = models.ImageField(upload_to='admin_app/projects')
    head = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    status = models.BooleanField(default=False)
    

class Message(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)