from django.contrib import admin

from goods.models import ProWomen,ProBaby

#admin.site.register(Products)

@admin.register(ProWomen)
class ProWomenAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(ProBaby)
class ProBabyAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
