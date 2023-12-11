from django.shortcuts import render


# Create your views here.
def cart_list(request):
    return render(request, "cart.html", {})


def add_cart(request):
    pass


def update_cart(request):
    pass


def delete_cart(request):
    pass
