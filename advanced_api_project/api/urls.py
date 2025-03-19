from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

# URLConf
urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
    path('authors/', views.Author_list),
    path('authors/<int:id>/', views.Author_detail),
]
