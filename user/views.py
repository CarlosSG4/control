from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PerfilesUpdateForm
from .models import Especialidades, perfiles
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