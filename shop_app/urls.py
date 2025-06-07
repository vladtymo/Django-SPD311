from django.contrib import admin
from django.urls import include, path

import products
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
]
