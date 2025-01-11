from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from main.models import Products


def index(request) -> HttpResponse:

    page= request.GET.get('page' ,1)
    order_by= request.GET.get('order_by' , None)

    main = Products.objects.all()
    if order_by and order_by != "default":
        main=main.order_by(order_by)

    paginator =Paginator(main, 6)
    current_page=paginator.page(int(page))
    context: dict[str, Any] = {
        'title': 'Home - Catalog',
        'main': current_page
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