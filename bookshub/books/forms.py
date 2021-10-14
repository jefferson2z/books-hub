from django.forms import ModelForm, TextInput, Textarea

from books.models import Genre, Book


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ("title",)
        widgets = {
            "title": TextInput(attrs={"class": "form-control input-lg"}),
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ("title", "isbn10", "isbn13", "description")
        widgets = {
            "title": TextInput(attrs={"class": "form-control input-lg"}),
            "isbn10": TextInput(attrs={"class": "form-control input-lg"}),
            "isbn13": TextInput(attrs={"class": "form-control input-lg"}),
            "description": Textarea(attrs={"class": "form-control input-lg"}),
        }
