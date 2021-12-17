from django.shortcuts import render


def user_login(request):
    return render(request, 'users/login.html')


def create_user(request):
    return render(request, 'users/create_user.html')
