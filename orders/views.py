from turtle import clear
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from cart.cart import clear_cart, get_cart
from orders.models import Order
from products.models import Product
from users.models import User

# Create your views here.


@login_required
def index(request):
    orders = Order.objects.all()

    # TODO: show only my
    orders = Order.objects.filter(client=request.user)

    return render(request, "orders/index.html", {"orders": orders})


def confirm(request):

    items = get_cart(request.session)

    if not items:
        messages.warning(request, "Your cart is empty!")
        return redirect("/cart")

    products = Product.objects.filter(id__in=items.keys())

    Order.objects.create(
        total_price=sum(p.price for p in products), client=User.objects.last()
    )

    clear_cart(request.session)

    return redirect("/orders")
