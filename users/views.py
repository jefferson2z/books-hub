from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render

from users.forms import CreateUserForm


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse("/"))
    else:
        form = CreateUserForm()
    return render(request, 'users/create.html', {"form": form})
