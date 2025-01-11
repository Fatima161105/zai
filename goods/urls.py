
from django.urls import path
from goods import views


app_name = 'goods'


urlpatterns: list = [
    path('women/', views.women, name='women'),
    path('baby/', views.baby, name='baby'),
    path('women/search/', views.women, name='search'),
    path('baby/search1/', views.baby, name='search1'),
    path('women/sproduct/<slug:product1_slug>/', views.sproduct, name='sproduct'),
    path('baby/sproduct/<slug:product2_slug>/', views.sproduct1, name='sproduct'),

    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]
