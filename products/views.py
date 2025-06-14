from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product


def index(request):
    # products = Product.objects.all()
    return render(request, "index.html")


def catalog(request):
    products = Product.objects.all().order_by("id")

    # products = [
    #     {"name": "Product 1", "price": 10.99},
    #     {"name": "Product 2", "price": 12.99},
    #     {"name": "Product 3", "price": 15.99},
    # ]

    return render(
        request, "catalog.html", {"products": products, "count": len(products)}
    )


def delete(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")

    itemToDelete = get_object_or_404(Product, pk=id)

    itemToDelete.delete()

    return redirect("/list")
