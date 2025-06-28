from django.shortcuts import redirect, render
from django.contrib import messages

from cart.cart import add_to_cart, clear_cart, get_cart
from products.models import Product


def index(request):
    items = get_cart(request.session)
    products = Product.objects.filter(id__in=items.keys())

    return render(request, "cart/index.html", {"products": products})


def add(request, id, quantity=1):
    if Product.objects.get(id=id) is None:
        messages.error(request, "Product not found!")
        return redirect("/cart")

    add_to_cart(request.session, id, quantity)
    messages.success(request, "Product added to cart!")

    return redirect("/cart")


def clear(request):
    clear_cart(request.session)
    messages.success(request, "Cart cleared!")

    return redirect("/cart")
