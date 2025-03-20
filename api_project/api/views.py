from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import request, response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):  # Extend ListAPIView
    queryset = Book.objects.all()  # Define the queryset
    serializer_class = BookSerializer  # Define the serializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the Book serializer
    permission_classes = [IsAuthenticated] 