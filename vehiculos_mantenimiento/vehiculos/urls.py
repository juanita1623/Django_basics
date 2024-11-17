from django.urls import path
from . import views

urlpatterns = [
    #ruta par crear un nuevo mantenimiento 
    path('crear/',views.crear_mantenimiento, name = 'crear_mantenimiento')
    # ver todos los mantenimientos 
    path('',views.lista_mantenimientos, name ='lista mantenimiento')
]