from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripción = models.TextField(verbose_name="descripción", null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio", default=0.00) 

    def __str__(self):
        fila = f"Título: {self.titulo} - Descripción: {self.descripción} - Precio: ${self.precio}"
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.user.username
   

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=100, verbose_name='Dia')
    horas = models.CharField(max_length=100, verbose_name='Horas')
    tipoContrato = models.CharField(max_length=100, verbose_name='TipoC')

    def __str__(self):
        fila = "id: " + self.id + " - " + "Tipo de contrato: " + self.tipoContrato
        return fila
    


