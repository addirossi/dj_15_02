from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import Product


def index_page(request):
    return render(request, 'main/index.html', {})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'prods': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'main/details.html', {'prod': product})
