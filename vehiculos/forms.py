from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AutosForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)



class CamionetasForm(forms.Form):
    marca = forms.CharField(max_length=50, required=True)
    modelo = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)



class MotosForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    color = forms.CharField(label="Color", max_length=50, required=True)
    precio = forms.IntegerField(label="Precio", required=True)



class CuatrisForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    color = forms.CharField(label="Color", max_length=50, required=True)
    precio = forms.IntegerField(label="Precio", required=True)



class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email de Registro")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Registro")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']



class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)