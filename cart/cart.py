from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        # Si hay una clave de sesion asignarla a la variable cart
        cart = self.session.get("session_key")

        # Si el usuario es nuevo y no hay clave generar una
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # hacer el carrito disponible para todas las paginas
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        # retornara la cantidad de elementos del carrito
        return len(self.cart)

    def get_products(self):
        # Obtener los Ids desde el carrito
        product_id = self.cart.keys()

        # buscar los IDs en la DB
        products = Product.objects.filter(id__in=product_id)
        # retornar la lista de productos
        return products
