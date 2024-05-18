from .views import *
from django.urls import path
urlpatterns = [
    path('', home, name='home'),
    path('base', base, name='base'),
    path('bodeguero/', bodeguero, name='bodeguero'),
    path('logout',logout_view,name='logout'),
    path('catalogo/',catalogo,name='catalogo'),
    path('autenticacion/',autenticacion,name='autenticacion'),
    path('contador/',contador,name='contador'),
    path('ventas/',ventas,name='ventas'),
    path('view_cart/',view_cart,name='view_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('view_cart/', view_cart, name='view_cart'),
     path('checkout/', checkout_view, name='checkout'),
     path('payment-success/', payment_success_view, name='payment-success'),
    path('payment-failed/', payment_failed_view, name='payment-failed'),

]