
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def bodeguero(request):
    return render(request, 'bodeguero.html')





def contador(request):
    return render(request, 'contador.html')
def ventas(request):
    return render(request, 'vendedor.html')


# Define la lista de usuarios
users = [
    {'username': 'bodeguero', 'password': '11111111-3'},
    {'username': 'vendedor', 'password': '11111111-3'},
    {'username': 'contador', 'password': '11111111-3'},
    {'username': 'administrador', 'password': '11111111-3'}
]

def autenticacion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        # Verificar las credenciales del usuario
        user = authenticate(request, username=usuario, password=contrasena)
        
        if user is not None:
            # Si las credenciales son correctas, iniciar sesión
            login(request, user)
            # Redirigir al usuario a la página de inicio
            return redirect('home')  # Cambia 'home' por el nombre de la URL de tu página de inicio
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error en la página de inicio de sesión
            return render(request, 'login.html', {'mensaje_error': True})

    # Si la solicitud no es de tipo POST, renderizar nuevamente la página de inicio de sesión
    return render(request, 'login.html')


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')  # Cambia 'home' por el nombre de la URL de tu página de inicio

def catalogo(request):
    api_url = "http://localhost:8000/Productoget.php"  # URL de tu API
    try:
            response = requests.get(api_url)
            response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
            data = response.json()  # Suponiendo que tu API devuelve una respuesta JSON
            products = data.get("records", [])  # Obtener los productos del JSON
            print(products)  # Imprimir los productos en la consola del servidor para depuración
    except requests.exceptions.RequestException as e:
            products = []
            error_message = str(e)
            print(error_message)  # Imprimir el mensaje de error en la consola del servidor para depuración

    return render(request, 'catalogo.html', {'products':products})




import requests
from django.http import JsonResponse
import requests
from django.shortcuts import render


import requests
from django.shortcuts import render, redirect, get_object_or_404



from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    response = requests.post(f"{settings.API_URL}/add_to_cart.php", json={'id_prod': product_id})
    if response.status_code == 200:
        product = response.json()
        if 'id_prod' in product:
            cart.add(product)
        else:
            return render(request, 'error.html', {'message': f"Error en la respuesta de la API: {response.json().get('message', 'Unknown error')}"})
    else:
        return render(request, 'error.html', {'message': f"Error al conectar con la API: {response.status_code} {response.text}"})
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    response = requests.get(f"{settings.API_URL}/get_one.php?id_prod={product_id}")
    if response.status_code == 200:
        product = response.json()
        cart.remove(product)
    return redirect('view_cart')

def view_cart(request):
    cart = Cart(request)
    return render(request, 'view_cart.html', {'cart': cart, 'total': cart.get_total_price()})

def catalog_view(request):
    response = requests.get(f"{settings.API_URL}/Productoget.php")
    if response.status_code == 200:
        products = response.json().get('records', [])
    else:
        products = []
    return render(request, 'catalogo.html', {'products': products})

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

def checkout_view(request):

    # Obtener los productos seleccionados del carrito de compras
    cart = Cart(request)
    cart_items = cart.cart_items
    cart_total = cart.get_total_price()

    # Obtener detalles de los productos desde la API o la base de datos
    product_details = []
    for item in cart_items:
        product_id = item['id']
        # Realizar una solicitud a la API o base de datos para obtener detalles del producto
        api_url = f"http://localhost:8000/Productoget.php?id={product_id}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                product_data = response.json()
                product_details.append(product_data)
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener detalles del producto {product_id}: {e}")

    host= request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': cart_total,
        'currency_code': 'USD',
        'item_name': 'Productos en el carrito de compras',
        'invoice': uuid.uuid4(),
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success')}",
        'cancel_url': f"http://{host}{reverse('payment-failed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'cart': cart_items,
        'total': cart_total,
        'transaction_id': paypal_checkout['invoice'],
        'paypal': paypal_payment,
    }

    return render(request, 'checkout.html')

def payment_success_view(request):
    cart = Cart(request)
    cart_items = cart.cart_items
    cart_total = cart.get_total_price()

    transaction_id = request.GET.get('tx')  # ID de la transacción de PayPal

    context = {
        'cart': cart_items,
        'total': cart_total,
        'transaction_id': transaction_id
    }

    # Vaciar el carrito después de una compra exitosa
    cart.clear()

    return render(request, 'payment-success.html', context)

def payment_failed_view(request):
    cart = Cart(request)
    cart_items = cart.cart_items
    cart_total = cart.get_total_price()

    transaction_id = request.GET.get('tx')  # ID de la transacción de PayPal, si está disponible

    context = {
        'cart': cart_items,
        'total': cart_total,
        'transaction_id': transaction_id
    }

    return render(request, 'payment-failed.html', context)
