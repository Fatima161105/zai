from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

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





