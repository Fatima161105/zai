from django.contrib import admin

from main.models import Products

#admin.site.register(Products)

@admin.register(Products)
class ProductsAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}