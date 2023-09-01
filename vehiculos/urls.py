from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', home, name="home" ),



    path('autos/', AutosList.as_view(), name="autos" ),
    path('create_autos/', AutosCreate.as_view(), name="create_autos" ),
    path('update_autos/<int:pk>/', AutosUpdate.as_view(), name="update_autos" ),
    path('delete_autos/<int:pk>/', AutosDelete.as_view(), name="delete_autos" ),
    path('buscar_autos/', buscarAutos, name="buscar_autos" ),
    path('buscar2/', buscar2, name="buscar2" ),



    path('camionetas/', CamionetasList.as_view(), name="camionetas" ),
    path('create_camionetas/', CamionetasCreate.as_view(), name="create_camionetas" ),
    path('update_camionetas/<int:pk>/', CamionetasUpdate.as_view(), name="update_camionetas" ),
    path('delete_camionetas/<int:pk>/', CamionetasDelete.as_view(), name="delete_camionetas" ),  



    path('motos/', MotosList.as_view(), name="motos" ),
    path('create_motos/', MotosCreate.as_view(), name="create_motos" ),
    path('update_motos/<int:pk>/', MotosUpdate.as_view(), name="update_motos" ),
    path('delete_motos/<int:pk>/', MotosDelete.as_view(), name="delete_motos" ),  



    path('cuatris/', CuatrisList.as_view(), name="cuatris" ),
    path('create_cuatris/', CuatrisCreate.as_view(), name="create_cuatris" ),
    path('update_cuatris/<int:pk>/', CuatrisUpdate.as_view(), name="update_cuatris" ),
    path('delete_cuatris/<int:pk>/', CuatrisDelete.as_view(), name="delete_cuatris" ),  



    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="vehiculos/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),



    path('about_me/', aboutMe, name="about_me" ),
]