from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.borrower.name} borrowed {self.book.title}'
