from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ['publication_year', 'author', 'title']
        
admin.site.register(Book, BookAdmin)   