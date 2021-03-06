from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='learn'),
    path('<str:tag>/', views.tag_archive),
    path('<str:tag>/<str:url_title>', views.details_page)
]
