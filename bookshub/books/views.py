from django.shortcuts import render
from books.models import Genre


def home_page(request):
    genres = Genre.objects.all()
    return render(request, "books/genres_list.html", {"genres": genres})


def genre_details(request, genre_id):
    return render(request, "books/genre_details.html")
