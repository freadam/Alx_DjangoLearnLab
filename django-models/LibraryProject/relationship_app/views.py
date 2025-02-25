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