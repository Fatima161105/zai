from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите имя пользователя"
        })
    )

    class Meta:
        model = User
        fields= ['email']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "autofocus": True,
            "class": "form-control",
            "placeholder": "Введите email"
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите номер телефона"
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Введите имя пользователя"
        })
    )

    class Meta:
        model = User
        fields = ["email", "phone", "username"]

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "phone",
            "email",
            "password",
            "username",
            "last_name",)
    image = forms.ImageField(required=False)
    phone = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    username = forms.CharField()
    last_name = forms.CharField(required=False)

    