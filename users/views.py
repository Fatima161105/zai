
from django.shortcuts import redirect, render

from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username= username, password=password)
            if user is not None:
                auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context: dict[str, str]={
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegistrationForm()

    context: dict[str, str]={

        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))