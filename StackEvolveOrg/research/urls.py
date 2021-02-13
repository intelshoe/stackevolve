from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tag>/', views.tag_archive),
    path('<str:tag>/<str:url_title>', views.article_details)
]
