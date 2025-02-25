# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView,user_login,user_logout,register  # Import list_books and LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
]

# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Login view with custom template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout view with custom template
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Register view
    path('register/', views.register, name='register'),
]