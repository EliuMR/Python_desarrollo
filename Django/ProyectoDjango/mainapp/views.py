from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',
                  {'title': 'Inicio',
                   'message': 'Bienvenido a la página de inicio de Django!'})

def about(request):
    return render(request, 'mainapp/about.html',
                  {'title': 'Acerca de',
                   'message': 'Bienvenido a la página de acerca de Django!'})

#Pagina de registro
def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        pass

    #register_form = UserCreationForm() #Se crea el formulario de registro
    #Utilizando mi formulario personalizado
    register_form = RegisterForm()
    if request.method == 'POST': #Si se envia el formulario
        #register_form = UserCreationForm(request.POST) #Se crea el formulario con los datos enviados
        #Utilizando mi formulario personalizado
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('index')
    return render(request, 'user/register.html',
                  {'title': 'Registro',
                   'bienvenida': 'Bienvenido a la página de registro de Django!',
                   'register_form': register_form

                   })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        pass
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.warning(request, 'Usuario o contraseña incorrecta')
    return render(request, 'user/login.html',
                  {'title': 'Inicio de sesión',
                   'bienvenida': 'Bienvenido a la página de inicio de sesión de Django!'})
 
#Cerrar sesión
def logout_user(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('index')
