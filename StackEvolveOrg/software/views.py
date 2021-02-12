from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Here you can download, preview, and contribute to \
        our amazing software projects!")
