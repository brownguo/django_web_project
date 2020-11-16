from django.shortcuts import render
from django.http import HttpResponse
import json
from blog import models

# Create your views here.


def HelloWorld(request):
    ctx = {
        "msg": "Hello World!"
    }
    return HttpResponse(json.dumps(ctx))


def Article(request, id):
    blog_article = models.Article.objects.all().order_by('-id')
    context = {
        'blog_article': blog_article,
        'article_id': id,
    }
    return render(request, 'article.html', context)