from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppTaro.models import *
from AppTaro.forms import *

# Create your views here.

def inicio(request):
    return render(request,"AppTaro/inicio.html")

def Cliente(request):
    return render(request,"AppTaro/clientes.html")

def Pedido(request):
    return render(request,"AppTaro/pedidos.html")

def Empleados(request):
    return render(request,"AppTaro/empleados.html")

def EmpleadoForm(request):
    if request.method == 'POST':
        miFormulario = empleadoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        edad = informacion['edad']
        cargo = informacion['cargo']
        Empleado = empleado(nombre=nombre,edad=edad,cargo=cargo)
        Empleado.save() # Guarda en la base de datos
        return render (request,"AppTaro/inicio.html")
    else:
        miFormulario = empleadoForm()
    return render(request,"AppTaro/empleadoForm.html",{'miFormulario':miFormulario})
        
def PedidoForm(request):
    if request.method == 'POST':
        miFormulario = pedidoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        cliente = informacion['cliente']
        empleado = informacion['empleado']
        fecha = informacion['fecha']
        Pedido = pedido(cliente=cliente,empleado=empleado,fecha=fecha)
        Pedido.save() # Guarda en la base de datos
        return render (request,"AppTaro/inicio.html")
    else:
        miFormulario = pedidoForm()
    return render(request,"AppTaro/pedidoForm.html",{'miFormulario':miFormulario})

def busquedaEmpleado(request):
    return render(request, "AppTaro/busquedaEmpleado.html")	
def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cargo = request.GET['cargo']
        Empleado = empleado.objects.filter(nombre=nombre,cargo=cargo)
        return render(request, "AppTaro/resultadoBusqueda.html", {'Empleado': Empleado, 'nombre': nombre, 'cargo': cargo})
    else:
        respuesta = "No se ingreso Nombre"
    return HttpResponse(respuesta)