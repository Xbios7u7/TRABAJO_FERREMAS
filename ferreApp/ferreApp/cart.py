from django.conf import settings
from .models import Producto

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, producto, quantity=1, override_quantity=False):
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {'quantity': 0, 'price': producto.precio}
        if override_quantity:
            self.cart[producto_id]['quantity'] = quantity
        else:
            self.cart[producto_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def __iter__(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        for producto in productos:
            self.cart[str(producto.id)]['producto'] = producto

        for item in self.cart.values():
            item['price'] = item['price']
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
