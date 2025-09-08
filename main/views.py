from django.shortcuts import render, redirect #aqui agregamos el redirect que es para redirreccionar



# Create your views here.

from .models import Curso

#from del registro
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate

##para poner mensajes
from django.contrib import messages

def homepage(request):
    return render(request, 'index.html', {"cursos":Curso.objects.all()})


##Registro Usuario

def register(request):
    #
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save() #guarda el usuario
            
            nombre_usuario = form.cleaned_data.get('username')#nuevo esto manda mensajes
            messages.success(request, f'Nueva Cuenta creada para: {nombre_usuario}')
            
            login(request, usuario) #logea al usuario
            return redirect('main:homepage') #redirecciona a la pagina principal
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}') ##msg es una llave para mostrar al usuario en caso de error
    #
    form = UserCreationForm()
    return render(request, 'registro.html', {"form":form}) #recomendable aca utilizar el mismo nombre en la variable


##para cerrar sesion
def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesion exitosamente")
    return redirect('main:homepage')

##para iniciar sesion
def login_request(request):
    form = AuthenticationForm() #esto es para que aparezca el formulario vacio
    render(request, 'login.html', {"form":form})