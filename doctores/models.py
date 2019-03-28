from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Consultorios(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField(default='default.jpg', upload_to='consul_pics')

    def __str__(self):
        return self.title

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField(default='default.jpg', upload_to='doctors_pics')
    genero = models.CharField(choices=(('Mujer', 'Mujer'), ('Hombre', 'Hombre')), max_length=16, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_celular = models.CharField(unique=True, max_length=10, null=True)    
    cedula = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)     

    def __str__(self):
        return self.name