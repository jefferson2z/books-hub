from django.shortcuts import render
from books.models import Genre, Book


def home_page(request):
    genres = Genre.objects.all()
    return render(request, "books/genres_list.html", {"genres": genres})


def genre_details(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    return render(request, "books/genre_details.html", {"genre": genre})


def books_list(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {"books": books})
