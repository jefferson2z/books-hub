from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("genres/<int:genre_id>/", views.genre_details, name="genre_details"),
    path("genres/new/", views.genre_form, name="genre_form"),
    path("books/<int:book_id>/", views.book_details, name="book_details"),
    path("books/new/", views.book_form, name="book_form"),
    path("books/", views.books_list, name="books_list"),
    path("", views.genres_list, name="genres_list"),
]
