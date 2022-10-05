from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    preserve_filters = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
