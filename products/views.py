from itertools import count
from django.shortcuts import render

from products.models import Product


def index(request):
    # products = Product.objects.all()
    return render(request, "index.html")


def catalog(request):
    products = Product.objects.all()

    # products = [
    #     {"name": "Product 1", "price": 10.99},
    #     {"name": "Product 2", "price": 12.99},
    #     {"name": "Product 3", "price": 15.99},
    # ]

    return render(
        request, "catalog.html", {"products": products, "count": len(products)}
    )
