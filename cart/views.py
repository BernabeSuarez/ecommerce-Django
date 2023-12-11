from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_list(request):
    return render(request, "cart.html", {})


def add_cart(request):
    # obtener el carrito
    cart = Cart(request)

    if request.POST.get("action") == "post":
        # obtener la data
        product_id = int(request.POST.get("product_id"))

        # buscar el producto en la DB
        product = get_object_or_404(Product, id=product_id)
        # guardarlo en la sesion
        cart.add(product=product)

        # obtener la cantidad de elemntos del carrito
        cart_quantity = cart.__len__()

        # retornar una respuesta
        response = JsonResponse({"quantity: ": cart_quantity})
        return response


def update_cart(request):
    pass


def delete_cart(request):
    pass
