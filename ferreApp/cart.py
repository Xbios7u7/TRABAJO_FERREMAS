from django.conf import settings

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product['id_prod'])
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product['id_prod'],
                'sku': product['sku'],
                'nom_producto': product['nom_producto'],
                'modelo': product['modelo'],
                'descripcion': product['descripcion'],
                'precio': str(product['precio']),
                'stock': product['stock'],
                'id_categoria': product['id_categoria'],
                'id_marca': product['id_marca'],
                'quantity': 1
            }
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product['id_prod'])
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(float(item['precio']) * item['quantity'] for item in self.cart.values())

    def __iter__(self):
        for item in self.cart.values():
            yield item

   
