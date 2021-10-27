from django.forms import ModelForm, TextInput, Textarea, ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple

from books.models import Genre, Book


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ("title",)
        widgets = {
            "title": TextInput(attrs={"class": "form-control input-lg"}),
        }


class BookForm(ModelForm):
    genres = ModelMultipleChoiceField(
        Genre.objects,
        widget=CheckboxSelectMultiple(
            attrs={"class": "form-check form-check-inline", "style": "list-style:none"}
        ),
    )

    class Meta:
        model = Book
        fields = ("title", "isbn10", "isbn13", "genres", "description")
        widgets = {
            "title": TextInput(attrs={"class": "form-control input-lg"}),
            "isbn10": TextInput(attrs={"class": "form-control input-lg"}),
            "isbn13": TextInput(attrs={"class": "form-control input-lg"}),
            "description": Textarea(attrs={"class": "form-control input-lg"}),
        }
