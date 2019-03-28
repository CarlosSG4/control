from django.shortcuts import render, redirect
from .models import Doctors, Consultorios

# Create your views here.
def doctores(request):  
    context ={
        'pos': Doctors.objects.all()
    }   
    return render(request, 'doctores/doc.html', context)

def consultorio(request):
    context ={
        'post': Consultorios.objects.all()
    }
    return render(request, 'doctores/consult.html', context)