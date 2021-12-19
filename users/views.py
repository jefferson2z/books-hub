from django.shortcuts import render


def create_user(request):
    return render(request, 'users/create_user.html')
