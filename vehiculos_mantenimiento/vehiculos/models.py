from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo =  models.CharField(max_length= 50)
    foto = models.ImageField(upload_to= 'fotos/')
    fecha_creacion =models.DateField(auto_now_add= True)

    def __str__(self):
        return str(self.nombre)
class mantenimiento (models.Model):
    Vehiculo = models.ForeignKey('vehiculo',on_delete= models.CASCADE)
    fecha =  models.DateField()
    observaciones = models.TextField()
    evidencia_fotografica = models.ImageField (upload_to= 'mantenimiento/fotos', blank=True, null= True)
    factura = models.FileField(upload_to='mantenmiento/facturas', blank= True, null= True)

    def __str__(self): 
        return f"Mantenimiento del {self.fecha} para {self.Vehiculo.nombre}"