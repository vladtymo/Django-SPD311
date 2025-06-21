from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("", views.index),
    path("list", views.catalog),
    path("create", views.create),
    path("edit/<int:id>", views.edit),
    path("delete/<int:id>", views.delete),
]
