from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default = '')
    
    
    
    
    
# 1. app => board
# 2. model => Article
# 3. id, title(VARCHAR 200), content(TextField)