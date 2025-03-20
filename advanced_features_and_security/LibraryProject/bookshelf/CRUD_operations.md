Book.objects.create(title = '1984',author ='George Orwell',publication_year = 1949)
<Book: Book object (1)>
Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
Book_to_update = Book.objects.filter(title='1984')
Book_to_update.update(title='Nineteen Eighty-Four')
1
Book_to_delete = Book.objects.get(title='Nineteen Eighty-Four') 
Book_to_delete.delete()
(1, {'bookshelf.Book': 1})