from django.contrib import admin
from .models import Vehiculo, mantenimiento

class MantemientoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo','fecha','observaciones_breve')

    def observaciones_breve(self,obj):
        return  obj.oberservaciones[:50]
    observaciones_breve.short_description = 'Observaciones'



# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(mantenimiento)
