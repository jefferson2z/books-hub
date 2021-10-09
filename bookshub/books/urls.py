from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("<int:genre_id>/", views.genre_details, name="genre_details"),
    path("", views.books_list, name="books_list"),
]
