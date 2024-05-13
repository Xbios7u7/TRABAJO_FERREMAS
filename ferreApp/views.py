
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def bodeguero(request):
    return render(request, 'bodeguero.html')



def catalogo(request):
    return render(request, 'catalogo.html')

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