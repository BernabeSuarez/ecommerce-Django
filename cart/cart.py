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

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {"price": str(product.price)}

        self.session.modified = True
