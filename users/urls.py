from django.urls import path
from django.contrib.auth import views as auth_views

from users import views

app_name = "users"
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html',
         next_page='/'), name="user-login"),
    path("create/", views.create_user, name="create-user")
]
