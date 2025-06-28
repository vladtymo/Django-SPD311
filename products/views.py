from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from products.forms.create import CreateProduct
from products.forms.edit import EditProduct
from products.models import Product
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    # products = Product.objects.all()
    return render(request, "index.html")


def catalog(request):
    products = Product.objects.all().order_by("id")

    page_number = request.GET.get("page", 1)
    page_size = request.GET.get("size", 5)

    # Get the page object
    page = Paginator(products, page_size).get_page(page_number)

    return render(
        request,
        "catalog.html",
        {
            "products": page.object_list,
            "total_count": len(products),
            "page": page,
            "page_size": page_size,
        },
    )


def create(request):
    # GET - відкриття сторінки для створеня
    # POST - створення продукту

    form = CreateProduct()

    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Product created successfully!")
            return redirect("/list")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "create.html", {"form": form})


def edit(request, id):
    product = Product.objects.get(id=id)

    if product is None:
        return HttpResponse("Product not found")

    form = EditProduct(instance=product)

    if request.method == "POST":
        form = EditProduct(request.POST, request.FILES, instance=product)

        # If the product has an image, delete the old one
        if request.FILES and product.image:
            product.image.delete(save=False)

        if form.is_valid():
            form.save()

            messages.success(request, "Product updated successfully!")
            return redirect("/list")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "edit.html", {"form": form})


def delete(request, id):
    if id <= 0:
        return HttpResponse("Invalid ID")

    itemToDelete = get_object_or_404(Product, pk=id)

    if itemToDelete.image:  # Check if the product has an image
        itemToDelete.image.delete(save=False)

    itemToDelete.delete()

    return redirect("/list")
