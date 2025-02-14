Book_to_delete = Book.objects.get(title='Nineteen Eighty-Four') 
Book_to_delete.delete()