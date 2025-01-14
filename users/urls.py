from django.urls import path
from users import views

app_name = 'users'

urlpatterns: list = [
      path('profile/', views.profile, name='profile'),
      path('login', views.login, name='login'),
      path('registration', views.registration, name='registration'),
      path('user/logout/', views.logout, name='logout')
]