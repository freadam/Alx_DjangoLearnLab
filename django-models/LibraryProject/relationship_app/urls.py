# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView,user_login,user_logout,register  # Import list_books and LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
