from django.shortcuts import render
from books.models import Genre


def home_page(request):
    genres = Genre.objects.all()
    return render(request, "books/genres_list.html", {"genres": genres})
