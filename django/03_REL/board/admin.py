from django.contrib import admin
from .models import Article

# Register your models here.

# Article 관리 가능
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']