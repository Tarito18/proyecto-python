from django.urls import path
from AppTaro.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('clientes/', Cliente, name='Clientes'),
    path('pedidos/', Pedido, name='Pedidos'),
    path('empleados/', Empleados, name='Empleados'),
    path('empleadoFform/', EmpleadoForm, name='EmpleadoForm'),
    path('pedidoForm/', PedidoForm, name='PedidoForm'),
    path('busquedaEmpleado/', busquedaEmpleado, name='busquedaEmpleado'),
    path('buscar/', buscar, name='buscar'),
]