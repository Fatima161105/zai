from django.shortcuts import redirect, render

from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm

def profile(request):
    context={
        'title': 'Home-Кабинет'
    }
    return render(request,'users/profile.html', context)

def login(request) -> HttpResponse:
    form = UserLoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:index'))  # Перенаправление на профиль
        else:
            messages.error(request, "Неправильный email или пароль.")  # Сообщение об ошибке
    else:
        print(form.errors)  # Лог ошибок формы

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    form = UserRegistrationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)  # Создаем пользователя, но не сохраняем сразу
        user.set_password(form.cleaned_data['password'])  # Устанавливаем пароль
        user.save()  # Сохраняем пользователя
        auth.login(request, user)  # Авторизуем пользователя
        return redirect(reverse('users:login'))  # Перенаправляем на профиль
    else:
        print(form.errors)  # Лог ошибок формы

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


def logout(request):
    ...