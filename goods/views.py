from django.shortcuts import render
from django.shortcuts import HttpResponse
from goods.models import ProWomen,ProBaby


def women(request) -> HttpResponse:
    goods=ProWomen.objects.all()
    context: dict[str, Any] = {
         
        'title': 'Home - Женская одежда',
        'content':"ЖЕНСКАЯ ОДЕЖДА",
        'goods': goods
    }
    return  render(request, 'goods/women.html', context)   

def baby(request) -> HttpResponse:
    goods=ProBaby.objects.all()
    context: dict[str, Any] = {
        'title': 'Home - Детская одежда',
        'content':"ДЕТСКАЯ ОДЕЖДА",
        'goods': goods
    }
    return  render(request, 'goods/baby.html', context) 

def sproduct(request, product1_slug) -> HttpResponse:
    sproducts = ProWomen.objects.get(slug=product1_slug)
    context: dict[str,ProWomen] ={
        'sproducts': sproducts
    }
    return  render(request, 'goods/sproduct.html', context=context)   

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
