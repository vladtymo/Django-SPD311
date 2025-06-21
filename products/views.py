from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.forms.create import CreateProduct
from products.models import Product


def index(request):
    # products = Product.objects.all()
    return render(request, "index.html")


def catalog(request):
    products = Product.objects.all().order_by("id")

    return render(
        request, "catalog.html", {"products": products, "count": len(products)}
    )


def create(request):
    # GET - відкриття сторінки для створеня
    # POST - створення продукту

    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)

        form.save()

        return redirect("/list")

    return render(request, "create.html", {"form": form})


def delete(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")

    itemToDelete = get_object_or_404(Product, pk=id)

    itemToDelete.delete()

    return redirect("/list")
