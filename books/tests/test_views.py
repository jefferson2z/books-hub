
from django.test import TestCase
from django.urls import reverse

from books.models import Book, Genre


class GenresListViewTest(TestCase):
    def test_uses_genres_list_template(self):
        response = self.client.get(reverse('books:genres-list'))
        self.assertTemplateUsed(response, "books/genres_list.html")

    def test_displays_existing_genre(self):
        Genre.objects.create(title="Fantasy")
        response = self.client.get(reverse('books:genres-list'))

        self.assertContains(response, "Fantasy")


class GenreDetailsViewTest(TestCase):
    def test_uses_genre_details_template(self):
        genre = Genre.objects.create(title="Fantasy")
        response = self.client.get(
            reverse('books:genre-details', args=[genre.id]))
        self.assertTemplateUsed(response, "books/genre_details.html")

    def test_display_correct_genre(self):
        genre = Genre.objects.create(title="Fantasy")
        response = self.client.get(
            reverse("books:genre-details", args=[genre.id]))

        self.assertContains(response, "Fantasy")
        self.assertContains(response, "Genre Fantasy")

    def test_display_correct_genre_books(self):
        first_genre = Genre.objects.create(title="Fantasy")

        first_book = Book()
        first_book.title = "Lord of the Rings"
        first_book.save()
        first_book.genres.add(first_genre)

        response = self.client.get(
            reverse('books:genre-details', args=[first_genre.id])
        )

        self.assertContains(response, "Fantasy")
        self.assertContains(response, "Lord of the Rings")


class BooksListViewTest(TestCase):
    def test_uses_books_list_template(self):
        response = self.client.get(reverse('books:books-list'))
        self.assertTemplateUsed(response, "books/books_list.html")

    def test_displays_existing_book(self):
        Book.objects.create(title="Les Miserables")
        response = self.client.get(reverse('books:books-list'))

        self.assertContains(response, "Les Miserables")
