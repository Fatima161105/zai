from django import template

from main.models import Products

register=template.Library()

@register.simple_tag()
def tag_products():
    return Products.objects.all()
