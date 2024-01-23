from django.contrib import admin
from .models import Category, Products


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 15
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductAdmin)
