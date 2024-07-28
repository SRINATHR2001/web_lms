from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/', views.list_books, name='list_books'),
    path('books/search/', views.search_books, name='search_books'),
    path('books/remove/<slug:book_slug>/', views.remove_book, name='remove_book'),
    path('books/borrow/<slug:book_slug>/', views.borrow_book, name='borrow_book'),
    path('books/return/<slug:book_slug>/', views.return_book, name='return_book'),

    path('authors/add/', views.add_author, name='add_author'),
    path('authors/', views.list_authors, name='list_authors'),
    path('authors/search/', views.search_authors, name='search_authors'),
    path('authors/remove/<int:pk>/', views.remove_author, name='remove_author'),

    path('borrowers/add/', views.add_borrower, name='add_borrower'),
    path('borrowers/', views.list_borrowers, name='list_borrowers'),
    path('borrowers/search/', views.search_borrowers, name='search_borrowers'),
    path('borrowers/remove/<int:pk>/', views.remove_borrower, name='remove_borrower'),
]
