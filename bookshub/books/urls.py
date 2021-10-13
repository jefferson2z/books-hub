from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("genres/<int:genre_id>/", views.genre_details, name="genre_details"),
    # path("/books/<int:genre_id>/", views.book_details, name="book_details"),
    path("books/", views.books_list, name="books_list"),
    path("", views.genres_list),
]
