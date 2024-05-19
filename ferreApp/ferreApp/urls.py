
from django.urls import path
from .views import *



urlpatterns = [

    path('', home, name='home'),
    path('base/', base, name='base'),
    path('bodeguero/', bodeguero, name='bodeguero'),
    path('autenticacion/', autenticacion, name='autenticacion'),
    path('contador/', contador, name='contador'),
    path('ventas/', ventas, name='ventas'),
    path('logout/', logout, name='logout'),
    path('catalogo/', catalogo, name='catalogo'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('checkout/', checkout, name='checkout'),
    path('checkout-view/', checkout_view, name='checkout_view'),
    path('payment-success/', payment_success_view, name='payment-success'),
    path('payment-failed/', payment_failed_view, name='payment-failed'),
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', carrito, name='carrito'),
]