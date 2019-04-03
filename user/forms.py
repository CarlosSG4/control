from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import perfiles, Agendar_cita


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class PerfilesUpdateForm(forms.ModelForm):
    class Meta:
        model = perfiles
        fields = ['nombre','apellidos','genero', 'email', 'fecha_nacimiento','numero_celular','curp',
        'direccion','municipio','estado','image']
class UserAgendaForm(forms.ModelForm):
    class Meta:
        model = Agendar_cita
        fields = ['nombre','apellidos','curp', 'genero', 'fecha','email','direccion',
        'municipio','estado','especialidad', 'doctor', 'consultorio', 'Turno', 'author']   