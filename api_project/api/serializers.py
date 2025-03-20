from rest_framework import serializers
from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=255)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # or list specific fields