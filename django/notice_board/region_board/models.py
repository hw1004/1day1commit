from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(50)
    content = models.CharField(10000)
    author = models.CharField(10)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)