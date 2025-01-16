from django.http import HttpResponse
from django.shortcuts import redirect, render
from carts.models import Cart
from main.models import Products

def cart_add(request, product_slug):
    product1 = Products.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product1)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product1, quantity=1)
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request,product_id):...
def cart_remove(request, cart_id):
    cart=Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
    
def cart(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Корзина',
        'content':"Корзина"
    }
    return  render(request, 'carts/cart.html', context)   