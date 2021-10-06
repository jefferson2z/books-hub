from django.test import TestCase
from books.models import Book, Genre, Author


class BookAndGenreModelsTest(TestCase):
    def test_saving_and_retrieving_genres(self):
        first_genre = Genre()
        first_genre.title = "Fantasy"
        first_genre.save()

        saved_genres = Genre.objects.all()
        self.assertEqual(saved_genres.count(), 1)
        self.assertEqual(saved_genres[0].title, "Fantasy")

    def test_saving_and_retrieving_books(self):
        first_book = Book()
        first_book.title = "Lord of the Rings"
        first_book.description = "A tale of friendship"
        first_book.isbn10 = "10"
        first_book.isbn13 = "13"
        first_book.save()

        saved_books = Book.objects.all()
        self.assertEqual(saved_books.count(), 1)
        self.assertEqual(saved_books[0].title, "Lord of the Rings")
        self.assertEqual(saved_books[0].description, "A tale of friendship")
        self.assertEqual(saved_books[0].isbn10, "10")
        self.assertEqual(saved_books[0].isbn13, "13")

    def test_saving_and_retrieving_authors(self):
        author = Author()
        author.name = "Tolkien"
        author.save()

        saved_authors = Author.objects.all()
        self.assertEqual(saved_authors.count(), 1)
        self.assertEqual(saved_authors[0].name, "Tolkien")

    def test_book_genre_relationship(self):
        first_book = Book()
        first_book.title = "Lord of the Rings"
        first_book.save()

        fantasy_genre = Genre()
        fantasy_genre.title = "Fantasy"
        fantasy_genre.save()

        first_book.genres.set([fantasy_genre])

        saved_books = Book.objects.all()
        self.assertEqual(saved_books[0].genres.all().count(), 1)

        book_genre = saved_books[0].genres.get(pk=1)
        self.assertEqual(book_genre.title, "Fantasy")

        saved_genres = Genre.objects.all()
        self.assertEqual(saved_genres[0].books.all().count(), 1)

        book = saved_genres[0].books.get(pk=1)
        self.assertEqual(book.title, "Lord of the Rings")

    def test_author_book_relationship(self):
        book = Book()
        book.title = "Lord of the Rings"
        book.save()

        author = Author()
        author.name = "Tolkien"
        author.save()

        book.authors.set([author])

        saved_book = Book.objects.get(title="Lord of the Rings")
        self.assertEqual(saved_book.authors.all().count(), 1)
