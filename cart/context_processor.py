from .cart import Cart

# crear un context process para que el carrito funcione en toda la aplicacion


def cart(request):
    # retornar la data defaut del carrito
    return {"cart": Cart(request)}
