from django.test import TestCase
from django.urls import reverse


class UserLoginView(TestCase):
    def test_uses_login_template(self):
        response = self.client.get(
            reverse('users:user-login'))
        self.assertTemplateUsed(response, 'users/login.html')
