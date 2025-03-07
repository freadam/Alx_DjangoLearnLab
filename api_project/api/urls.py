from django.urls import path
from django.urls import path
from django.contrib import admin
from django.urls import path, include  # Include function for app URLs
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [ 
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval URL
]
