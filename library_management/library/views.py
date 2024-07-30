from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Book, Author, Borrower, BorrowedBook
from .forms import BookForm, AuthorForm, BorrowerForm

def dashboard(request):
    return render(request, 'library/dashboard.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})

def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(genre__icontains=query)
        )
    else:
        books = Book.objects.all()

    return render(request, 'library/list_books.html', {'books': books})

def remove_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    if not book.is_borrowed:
        book.delete()
    return redirect('list_books')

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_authors')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'library/list_authors.html', {'authors': authors})

def search_authors(request):
    query = request.GET.get('q')
    authors = Author.objects.filter(name__icontains=query)
    return render(request, 'library/list_authors.html', {'authors': authors})

def remove_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if author.book_set.count() == 0:
        author.delete()
    return redirect('list_authors')

def add_borrower(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_borrowers')
    else:
        form = BorrowerForm()
    return render(request, 'library/add_borrower.html', {'form': form})

def list_borrowers(request):
    borrowers = Borrower.objects.all()
    return render(request, 'library/list_borrowers.html', {'borrowers': borrowers})

def search_borrowers(request):
    query = request.GET.get('q')
    borrowers = Borrower.objects.filter(name__icontains=query)
    return render(request, 'library/list_borrowers.html', {'borrowers': borrowers})

def remove_borrower(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)
    if borrower.borrowedbook_set.count() == 0:
        borrower.delete()
    return redirect('list_borrowers')

def borrow_book(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    if book.is_borrowed:
        return redirect('list_books')
    if request.method == 'POST':
        borrower_id = request.POST.get('borrower_id')
        borrower = get_object_or_404(Borrower, id=borrower_id)
        BorrowedBook.objects.create(book=book, borrower=borrower)
        book.is_borrowed = True
        book.save()
        return redirect('list_books')
    borrowers = Borrower.objects.all()
    return render(request, 'library/borrow_book.html', {'book': book, 'borrowers': borrowers})

def return_book(request, book_slug):
    borrowed_book = get_object_or_404(BorrowedBook, book__slug=book_slug)
    book = borrowed_book.book
    book.is_borrowed = False
    book.save()
    borrowed_book.delete()
    return redirect('list_books')
