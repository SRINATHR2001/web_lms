from django.contrib import admin
from .models import Book, Author, Borrower, BorrowedBook

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Borrower)
admin.site.register(BorrowedBook)
