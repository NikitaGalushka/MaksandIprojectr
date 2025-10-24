from django.shortcuts import render
from .models import *
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required






def main(request):
    return render(request, 'TronHTML/main.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()

    return render(request, "TronHTML/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Авторизація Успішна')
                return redirect('/')  # Redirect to the homepage
            else:
                messages.error(request, 'Логин не правильний')
        else:
            messages.error(request, 'Пароль не правильний')
    else:
        form = AuthenticationForm()

    return render(request, 'TronHTML/login.html', {'form': form})