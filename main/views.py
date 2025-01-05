from django.shortcuts import render

def index(request) -> HttpResponse:
    return HttpResponse(request, 'main/index.html')

def about(request) -> HttpResponse:
    return HttpResponse('About page')    
