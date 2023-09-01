from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def home(request):
    return render(request, "vehiculos/home.html")



class CamionetasList(LoginRequiredMixin, ListView):
    model = Camionetas

class CamionetasCreate(LoginRequiredMixin, CreateView):
    model = Camionetas
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('camionetas')

class CamionetasUpdate(LoginRequiredMixin, UpdateView):
    model = Camionetas
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('camionetas')

class CamionetasDelete(LoginRequiredMixin, DeleteView):
    model = Camionetas
    success_url = reverse_lazy('camionetas')



class AutosList(LoginRequiredMixin, ListView):
    model = Autos

class AutosCreate(LoginRequiredMixin, CreateView):
    model = Autos
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('autos')

class AutosUpdate(LoginRequiredMixin, UpdateView):
    model = Autos
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('autos')

class AutosDelete(LoginRequiredMixin, DeleteView):
    model = Autos
    success_url = reverse_lazy('autos')

@login_required
def buscarAutos(request):
    return render(request, "vehiculos/buscarAutos.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        autos = Autos.objects.filter(marca__icontains=patron)
        contexto = {"autos": autos}
        return render(request, "vehiculos/autos.html", contexto)
    return HttpResponse("Usted no Ingreso Ningun Dato a Buscar")



class MotosList(LoginRequiredMixin, ListView):
    model = Motos

class MotosCreate(LoginRequiredMixin, CreateView):
    model = Motos
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('motos')

class MotosUpdate(LoginRequiredMixin, UpdateView):
    model = Motos
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('motos')

class MotosDelete(LoginRequiredMixin, DeleteView):
    model = Motos
    success_url = reverse_lazy('motos')



class CuatrisList(LoginRequiredMixin, ListView):
    model = Cuatris

class CuatrisCreate(LoginRequiredMixin, CreateView):
    model = Cuatris
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('cuatris')

class CuatrisUpdate(LoginRequiredMixin, UpdateView):
    model = Cuatris
    fields = ['marca', 'modelo', 'color', 'precio']
    success_url = reverse_lazy('cuatris')

class CuatrisDelete(LoginRequiredMixin, DeleteView):
    model = Cuatris
    success_url = reverse_lazy('cuatris')



def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar   
                return render(request, "vehiculos/base.html", {'mensaje': f'Bienvenido a la página de venta {usuario}'})
            else:
                return render(request, "vehiculos/login.html", {'form': miForm, 'mensaje': f'Los datos no son validos'})
        else:
            return render(request, "vehiculos/login.html", {'form': miForm, 'mensaje': f'Los datos no son validos'})
    miForm = AuthenticationForm()
    return render(request, "vehiculos/login.html", {"form":miForm}) 



def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "vehiculos/base.html") 
    else:
        miForm = RegistroUsuariosForm()
    return render(request, "vehiculos/registro.html", {"form":miForm}) 



@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "vehiculos/base.html")
        else:
            return render(request, "vehiculos/editarPerfil.html", {'form':form, 'usuario':usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "vehiculos/editarPerfil.html", {'form':form, 'usuario':usuario.username})  



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()  
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "vehiculos/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "vehiculos/agregarAvatar.html", {'form':form})     



def aboutMe(request):
    return render(request, "vehiculos/aboutMe.html")