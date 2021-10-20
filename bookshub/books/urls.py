from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("genres/<int:genre_id>/", views.genre_details, name="genre-details"),
    path("genres/new/", views.genre_form, name="new-genre-form"),
    path("books/<int:book_id>/", views.book_details, name="book-details"),
    path("books/new/", views.book_form, name="new-book-form"),
    path("books/", views.books_list, name="books-list"),
    path("", views.genres_list, name="genres-list"),
]
