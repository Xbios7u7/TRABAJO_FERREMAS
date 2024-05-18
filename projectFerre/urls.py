
from django.contrib import admin
from django.urls import path, include
from ferreApp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('', include('paypal.standard.ipn.urls')),
]
