from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

# homepage content
def index(request):
    return HttpResponse("Welcome to our research \
        publications, tutorials, and experiments!")

# Catagory page content
def tag_archive(request, tag):
    arts = Article.objects.filter(tag=tag)
    context ={'tag' : tag, 'article_list': arts}
    return render(request, 'learn/tags_archive.html', context)

# Article detail pages
def details_page(request, url_title):
    a_list = Article.objects.filter(article_title)
    return HttpResponse(a_list)
