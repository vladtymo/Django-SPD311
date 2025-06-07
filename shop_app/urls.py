from django.contrib import admin
from django.urls import path

import products
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index", views.index),
    path("list", views.catalog),
]
