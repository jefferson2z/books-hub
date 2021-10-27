from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from books.models import Genre, Book
from books.forms import GenreForm, BookForm


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, "books/genres_list.html", {"genres": genres})


def genre_details(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    books = genre.books.all()
    return render(request, "books/genre_details.html", {"genre": genre, "books": books})


def genre_form(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            Genre.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse("books:genres-list"))
    else:
        form = GenreForm()
    return render(
        request,
        "create_form.html",
        {"title": "Genre", "action": "/genres/new/", "form": form},
    )


def books_list(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {"books": books})


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/book_details.html", {"book": book})


def book_form(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("books:books-list"))
    else:
        form = BookForm()
    return render(
        request,
        "create_form.html",
        {"title": "Book", "action": "/books/new/", "form": form},
    )
