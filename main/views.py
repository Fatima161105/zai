
from django.contrib import auth, messages
from typing import Any
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from main.models import Products
from main.utils import q_search
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm


def index(request) -> HttpResponse:
    
    page= request.GET.get('page' ,1)
    order_by= request.GET.get('order_by' , None)
    query= request.GET.get('q' , None)

    main = Products.objects.all()
    if query:
        main=q_search(query)

    if order_by and order_by != "default":
        main=main.order_by(order_by)

    paginator =Paginator(main, 6)
    current_page=paginator.page(int(page))
    context: dict[str, Any] = {
        'title': 'Home - Catalog',
        'main': current_page,
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content':"О нас"
    }
    return  render(request, 'main/about.html', context) 

def sproduct2(request, product_slug) -> HttpResponse:
   
    sproducts1 =  Products.objects.get(slug=product_slug) 

    context: dict[str,Products] ={
        'sproducts1': sproducts1
        
    }
    return  render(request, 'main/sproduct1.html', context=context) 

