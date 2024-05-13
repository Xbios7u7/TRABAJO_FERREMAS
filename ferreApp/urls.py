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
 
    
    

]