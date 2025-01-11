from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from main.models import Products
from main.utils import q_search
from django.contrib import auth
from django.urls import reverse
from main.forms import UserLoginForm

def index(request) -> HttpResponse:
    if request.method =='POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form=UserLoginForm()
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
        'form':form
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

def login(request):
    context={
        'title': 'Home-Авторизация'
    }
    return render(request,'main/login.html', context)

def registration(request):
    context={
        'title': 'Home-Регистрация'
    }
    return render(request,'main/registration.html', context)
    
def logout(request):
    ...