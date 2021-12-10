
from django.test import TestCase


class GenreFormTest(TestCase):
    def test_uses_genre_form_template(self):
        response = self.client.get("/genres/new/")
        self.assertTemplateUsed(response, "create_form.html")
