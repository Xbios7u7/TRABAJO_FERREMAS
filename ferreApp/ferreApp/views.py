from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout

from .cart import Cart
import requests
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid

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

def logout_view(request):
    logout(request)
    return redirect('home')


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


def catalogo(request):
    api_url = "http://localhost:8000/api/Productoget.php"  # URL de tu API
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
        data = response.json()  # Suponiendo que tu API devuelve una respuesta JSON
        products = data.get("records", [])  # Obtener los productos del JSON
        print(products)  # Imprimir los productos en la consola del servidor para depuración
    except requests.exceptions.RequestException as e:
        products = []
        error_message = str(e)
        print(f"Error fetching data from API: {error_message}")  # Imprimir el mensaje de error en la consola del servidor para depuración

    return render(request, 'catalogo.html', {'products': products})

API_URL = "http://localhost:8000/api/Productoget.php"



import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

API_URL = "http://localhost:8000/api/postCarrito.php"

@csrf_exempt
def agregar_al_carrito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'error': 'Error al agregar al carrito'}, status=500)
    return JsonResponse({'error': 'Método no permitido'}, status=405)



def carrito(request):
   return render(request, 'carrito.html')




def checkout(request):
    cart = Cart(request)
    cart_items = list(cart)
    cart_total = cart.get_total_price()

    # Obtener detalles de los productos desde la API o la base de datos
    product_details = []
    for item in cart_items:
        product_id = item['producto'].id
        api_url = f"http://localhost:8000/Productoget.php?id={product_id}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                product_data = response.json()
                product_details.append(product_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching product data: {e}")
    
    context = {
        'cart': cart,
        'cart_total': cart_total,
        'product_details': product_details
    }

    return render(request, 'checkout.html', context)

def checkout_view(request):
    cart = Cart(request)
    cart_items = list(cart)
    cart_total = cart.get_total_price()

    product_details = []
    for item in cart_items:
        product_id = item['producto'].id
        api_url = f"http://localhost:8000/Productoget.php?id={product_id}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                product_data = response.json()
                product_details.append(product_data)
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener detalles del producto {product_id}: {e}")

    host = request.get_host()

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

    return render(request, 'checkout.html', context)

def payment_success_view(request):
    cart = Cart(request)
    cart_items = list(cart)
    cart_total = cart.get_total_price()

    transaction_id = request.GET.get('tx')

    context = {
        'cart': cart_items,
        'total': cart_total,
        'transaction_id': transaction_id
    }

    cart.clear()

    return render(request, 'payment-success.html', context)

def payment_failed_view(request):
    cart = Cart(request)
    cart_items = list(cart)
    cart_total = cart.get_total_price()

    transaction_id = request.GET.get('tx')

    context = {
        'cart': cart_items,
        'total': cart_total,
        'transaction_id': transaction_id
    }

    return render(request, 'payment-failed.html', context)
