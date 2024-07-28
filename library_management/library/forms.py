from django import forms
from .models import Book, Author, Borrower

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name', 'email']
