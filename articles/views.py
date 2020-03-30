from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def articles(request):
    article = Article.objects.all().order_by('date')
    return render(request, 'articles/article.html', {'articles': article})


def article_detail(request, slug):
    article=Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':article})