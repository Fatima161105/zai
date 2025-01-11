from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from goods.models import ProWomen,ProBaby


def women(request) -> HttpResponse:
    page=request.GET.get('page',1)
    order_by= request.GET.get('order_by' , None)

    goods=ProWomen.objects.all()
    if order_by and order_by != "default":
        goods=goods.order_by(order_by)

    paginator =Paginator(goods,6)
    current_page=paginator.page(int(page))
    context: dict[str, Any] = {
         
        'title': 'Home - Женская одежда',
        'content':"ЖЕНСКАЯ ОДЕЖДА",
        'goods': current_page
    }
    return  render(request, 'goods/women.html', context)   

def baby(request) -> HttpResponse:
    page=request.GET.get('page',1)
    order_by= request.GET.get('order_by' , None)

    goods=ProBaby.objects.all()
    if order_by and order_by != "default":
        goods=goods.order_by(order_by)

    paginator =Paginator(goods,6)
    current_page=paginator.page(int(page))

    context: dict[str, Any] = {
        'title': 'Home - Детская одежда',
        'content':"ДЕТСКАЯ ОДЕЖДА",
        'goods': current_page
    }
    return  render(request, 'goods/baby.html', context) 

def sproduct(request, product1_slug,) -> HttpResponse:
   
    sproducts =  ProWomen.objects.get(slug=product1_slug) 

    context: dict[str,ProWomen] ={
        'sproducts': sproducts
        
    }
    return  render(request, 'goods/sproduct.html', context=context) 

def sproduct1(request, product2_slug,) -> HttpResponse:
   
    sproducts =  ProBaby.objects.get(slug=product2_slug) 

    context: dict[str,ProBaby] ={
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

