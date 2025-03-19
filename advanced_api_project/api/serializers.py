import datetime
from rest_framework import serializers
from .models import Author, Book

# serializer for Book model containing the title, publication year and nested serialization of the author
class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
        # validation for publication_year
        # publication_year cannot be in the future 
        def validate(self, data):
            current_year = datetime.now().year
            if data['publication_year'] > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return data
        
# serializer for Author model containing the name of the author and books
class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255,source='author.name')
    books = BookSerializer(many=True, read_only=True) 
    class Meta:
        model = Author
        fields = ['name', 'books']
        
