from django.test import TestCase


class UserLoginView(TestCase):
    def test_uses_login_template(self):
        response = self.client.get('/users/login/')
        self.assertTemplateUsed(response, 'users/login.html')
