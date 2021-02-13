from django.shortcuts import render
from django.http import HttpResponse

# homepage content
def index(request):
    return HttpResponse("Welcome to our research \
        publications, tutorials, and experiments!")

# Catagory page content
def tag_archive(request, tag):
    a_list = Article.objects.filter(tag)
    return HttpResponse(a_list)

# Article detail pages
def details_page(request, url_title):
    a_list = Article.objects.filter(article_title)
    return HttpResponse(a_list)
