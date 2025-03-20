from django.contrib import admin
from .models import Book, Library,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')  # Display the id field

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display the id field

admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Author)
