from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_list, name="cart_list"),
    path("add/", views.add_cart, name="add_cart"),
    path("update/", views.update_cart, name="update_cart"),
    path("delete/", views.delete_cart, name="delete_cart"),
]
