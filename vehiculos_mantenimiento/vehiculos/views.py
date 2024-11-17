from django.shortcuts import render,redirect
from .models import Mantenimiento
from .forms import MantenimientoForm


# Create your views here.
# crear vista mantenimiento

def crear_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    
    else: 
        form = MantenimientoForm()
    return render (request,'vehiculo/ crear_mantenimiento.html',{form:form})

def listar_mantenimientos(request):
    #obtener los mantenimientos 
    mantenimientos = Mantenimiento.objects.all()
    return render (request,'vehiculos/ lista_mantenimientos.html',{'mantenimientos': mantenimientos})
