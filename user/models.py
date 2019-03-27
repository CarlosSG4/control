from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class perfiles(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.ImageField(default='default.jpg', upload_to='profile_pics')
    genero = models.CharField(choices=(('M', 'Mujer'), ('H', 'Hombre')), max_length=16, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    numero_celular = models.CharField(unique=True, max_length=10, null=True)    
    curp = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)    
    direccion = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)    

    
    def __str__(self):
        return self.nombre
  
class Especialidades(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField(default='default.jpg', upload_to='espec_pics')

    def __str__(self):
        return self.title


