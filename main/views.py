from django.shortcuts import render
from django.shortcuts import HttpResponse
from main.models import Products


def index(request) -> HttpResponse:
    main = Products.objects.all()
    context: dict[str, Any] = {
        'title': 'Home - Catalog',
        }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content':"О нас"
    }
    return  render(request, 'main/about.html', context) 

