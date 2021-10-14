from django.forms import ModelForm, TextInput

from books.models import Genre


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ("title",)
        widgets = {
            "title": TextInput(attrs={"class": "form-control input-lg"}),
        }
