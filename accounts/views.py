from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import AuthUser
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = AuthUser

        fields = (
            "username",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasque:index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
