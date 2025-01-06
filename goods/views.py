from django.shortcuts import render
from django.shortcuts import HttpResponse



def women(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Женская одежда',
        'content':"ЖЕНСКАЯ ОДЕЖДА"
    }
    return  render(request, 'goods/women.html', context)   

def baby(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Детская одежда',
        'content':"ДЕТСКАЯ ОДЕЖДА"
    }
    return  render(request, 'goods/baby.html', context) 

def sproduct(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Карточка товара',
        'content':""
    }
    return  render(request, 'goods/sproduct.html', context)   

def cart(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Корзина',
        'content':"Корзина"
    }
    return  render(request, 'goods/cart.html', context)   

def checkout(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Оформление заказа',
        'content':"Оформление заказа"
    }
    return  render(request, 'goods/checkout.html', context)   
