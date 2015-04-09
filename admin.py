from django.contrib import admin
from article.models import Article, Comments

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title', 'article_text', 'article_date']
	list_filter = ['article_date']
	
admin.site.register(Article, ArticleAdmin)
