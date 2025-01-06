from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Catalog',
        'content':"КАТАЛОГ"
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content':"О нас"
    }
    return  render(request, 'main/about.html', context) 

