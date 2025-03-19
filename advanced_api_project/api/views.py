from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer
from .models import Author, Book

# Create your views here.
@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def book_detail(request, id):
    book = get_object_or_404(Book,id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view()
def Author_list(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def Author_detail(request, id):
    author = get_object_or_404(Author,id=id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)