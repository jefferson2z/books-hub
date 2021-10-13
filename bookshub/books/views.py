from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from books.models import Genre, Book


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, "books/genres_list.html", {"genres": genres})


def genre_details(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    return render(request, "books/genre_details.html", {"genre": genre})


def genre_form(request):
    if request.method == "POST":
        Genre.objects.create(title=request.POST['title'])
        return HttpResponseRedirect(reverse('books:genres_list'))
    else:
        return render(request, "books/genre_form.html")


def books_list(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {"books": books})


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/book_details.html", {"book": book})
