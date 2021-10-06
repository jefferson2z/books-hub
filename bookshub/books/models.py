from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}, ID: {self.id}"


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.title}, ID: {self.id}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    isbn10 = models.CharField(max_length=10, blank=True)
    isbn13 = models.CharField(max_length=13, blank=True)
    genres = models.ManyToManyField(Genre, related_name="books", blank=True)
    authors = models.ManyToManyField(Author, related_name="authors", blank=True)

    def __str__(self) -> str:
        return f"{self.title}, ID: {self.id}"
