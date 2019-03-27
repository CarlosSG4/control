from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class medicos(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    image =models.ImageField(default='default.jpg', upload_to='docs_pics')
    genero = models.CharField(choices=(('Mujer', 'Mujer'), ('Hombre', 'Hombre')), max_length=16, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_celular = models.CharField(unique=True, max_length=10, null=True)    
    cedula = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)    
    
    def __str__(self):
        return self.nombre