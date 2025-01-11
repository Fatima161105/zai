from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    email =forms.CharField()
    password = forms.CharField()
 #email =forms.CharField(
#     widget=forms.TextInput(attrs ={"autofocus": True,
#                                     'class':'form-control',
#                                     'placeholder': 'Введите email или номер телефона'})
# )
#password = forms.CharField(
#    widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
  #                                     'class':'form-control',
  #                                     'placeholder': 'Введите ваш пароль'})

    class Meta:
        model = User
        fieds=['username','password']
