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


class Agendar_cita(models.Model):
    nombre = models.OneToOneField(perfiles, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=20)
    curp = models.CharField(max_length=20)
    genero = models.CharField(choices=(('Mujer', 'Mujer'), ('Hombre', 'Hombre')), max_length=16, blank=True) 
    fecha = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    especialidad = models.OneToOneField(Especialidades, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    consultorio = models.OneToOneField(Consultorios, on_delete=models.CASCADE)
    Turno = models.CharField(choices=(('Matutino', 'Matutino'), ('Vespertino', 'Vespertino')), max_length=16, blank=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre
