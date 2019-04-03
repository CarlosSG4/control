from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PerfilesUpdateForm, UserAgendaForm
from .models import Especialidades, perfiles, Doctors, Consultorios, Agendar_cita
#funcion de registro manda en automatico el formulario
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada satisfactoriamente porfavor inicia sesion!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render (request, 'user/register.html', {'form': form})

#esto sirve para poder visualizar los archivos html con django
@login_required
def profile(request):
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilesUpdateForm(request.POST, request.FILES, instance=request.user.perfiles)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Tu perfil ha sido Actualizado!')
            return redirect('profile')            

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilesUpdateForm(instance=request.user.perfiles)        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/updateperfil.html', context)

def especialidades(request):
    context ={
        'post': Especialidades.objects.all()
    }
    return render(request, 'user/espec.html', context)

def perfil(request):   
    return render(request, 'user/perfil.html')

def doctores(request):  
    context ={
        'pos': Doctors.objects.all()
    }   
    return render(request, 'user/doc.html', context)

def consultorio(request):
    context ={
        'post': Consultorios.objects.all()
    }
    return render(request, 'user/consult.html', context)

def agendar(request):
    if request.method == 'POST': 
        a_form = UserAgendaForm(request.POST)
        if a_form.is_valid() :
            a_form.save()
            messages.success(request, f'Tu Cita a sido marcada!')
            return redirect('agendar')            

    else:
        a_form = UserAgendaForm()        
    context = {
        'a_form': a_form
    }

    return render(request, 'user/agendar_cita.html', context)

def mis_citas(request):  
    context ={
        'pots': Agendar_cita.objects.filter()
    }   
    return render(request, 'user/mis_citas.html', context)