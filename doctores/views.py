from django.shortcuts import render, redirect
from .models import medicos

# Create your views here.
def medicos(request):     
    return render(request, 'doctores/doc.html')

