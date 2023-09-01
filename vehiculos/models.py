from django.db import models
from django.contrib.auth.models import User



class Autos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}"



class Camionetas(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Camioneta"
        verbose_name_plural = "Camionetas"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}"  
    

    
class Motos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}" 
    
    
    
class Cuatris(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Cuatri"
        verbose_name_plural = "Cuatris"
        ordering = ['-marca']

    def __str__(self):
        return f"{self.marca} - {self.modelo}" 
    


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"