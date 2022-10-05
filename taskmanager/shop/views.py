from django.shortcuts import render, get_object_or_404
from .models import Category, Product

"""отображает список продуктов"""


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products =Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


"""Отображение в отдельном окне, для подробного ознакомления с товаром"""


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

# Create your views here.
