
from django.urls import path
from main import views

app_name = 'main'

urlpatterns: list = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('sproduct1/<slug:product_slug>/', views.sproduct2, name='sproduct1'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
     
]



