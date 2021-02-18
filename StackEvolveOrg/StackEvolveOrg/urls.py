"""StackEvolveOrg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from about import urls
from questions import urls
from learn import urls
from software import urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', include('about.urls'), name='index'),
    path('ask/', include('questions.urls'), name='index'),
    path('learn/', include('learn.urls'), name='index'),
    path('software/', include('software.urls'), name='index'),
    path('admin/', admin.site.urls),
]
