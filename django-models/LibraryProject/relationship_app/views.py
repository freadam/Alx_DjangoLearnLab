# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book, Library  # Adjust the model import as needed

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_details(request, id):
    library = get_object_or_404(Library, id=id)  # Get the library with the given id
    return render(request, 'relationship_app/library_details.html', {'library': library})


# relationship_app/views.py
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library  # Adjust the model import as needed

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form}) 

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a home page or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Adjust redirect as needed
        return render(request, 'relationship_app/register.html', {'form': form})