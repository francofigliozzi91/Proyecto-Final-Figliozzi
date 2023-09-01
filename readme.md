Proyecto Final Figliozzi, Franco Curso Python Coderhouse (Comisión: 55630)

ProyectoFinal es una aplicación web desarrollada en Django que permite a los usuarios registrarse, ingresar y salir de la app. La finalidad de la app es el control de stock de vehiculos divididos en 4 clases (autos, camionetas, motos y cuatris), cada clase cuenta con 4 atributos (marca, modelo, color y precio).
El sistema de autenticación y autorización restringe el acceso a ciertas funciones a usuarios no registrados. 
Incluye también un sistema de edición de perfil y manejo de los avatars, como también un apartado de admin donde se puede manejar toda la pagina (Usuario: admin; Password: 12345).
En lo relativo al html base, se utilizo el Grayscale de BootStrap (https://startbootstrap.com/previews/grayscale) editado para brindar sencillez en la interfaz.

Funcionalidades de la app:

A continuación se detallan las funcionalidades de ProyectoFinal:

Registro y autenticación:

    Los usuarios pueden registrarse haciendo click en "REGISTRO".
    Los usuarios pueden iniciar sesión en "LOGIN".
    Los usuarios pueden cerrar sesión en la aplicación en cualquier momento en "LOGOUT".

Lista de vehiculos:
    Los usuarios pueden agregar vehiculos (autos, camionetas, motos y cuatris) definiendo sus caracteristicas (marca, modelo, color y precio) haciendo click en "+", una vez agregado lo pueden "editar" y "eliminar".
    
Búsqueda de vehiculos (autos):
    Los usuarios pueden buscar autos agregados en la base de datos.

Perfil:
    Los usuarios pueden editar su perfil haciendo click en " Mi Perfil" (email, nombre, apellido y password).

Administración:
    Los usuarios con permisos de administrador pueden ver, editar, eliminar y agregar todo. (Usuario: admin; Password: 12345).
	
AboutMe
    Cualquiera que entre a la página puede ver el AboutMe sobre el creador de la página.