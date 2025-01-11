from django.urls import path
from users import views

app_name = 'users'

urlpatterns: list = [
      path('profile/', views.profile, name='profile'),
]