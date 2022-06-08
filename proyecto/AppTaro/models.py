from django.db import models

# Create your models here.
class empleado(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + self.cargo

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + self.direccion

class pedido(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    def __str__(self):
        return self.cliente.nombre + " " + self.empleado.nombre + " " + str(self.fecha)
        