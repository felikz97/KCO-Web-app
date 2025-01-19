from django.db import models
from django.contrib.auth.models import AbstractUser



class Post(models.Model):
    title= models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Usar(models.Model):
    username=models.CharField(max_length=10)
    name=models.CharField(max_length=52)
    email=models.CharField(max_length=15)
    Adm = models.CharField(max_length=20)
   
