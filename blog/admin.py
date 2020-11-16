# Register your models here.
from django.contrib import admin
from .models import Article, Tags, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_time',)
    list_display_links = ['title']


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_title = '才智小天地'
admin.site.site_header = '才智小天地'