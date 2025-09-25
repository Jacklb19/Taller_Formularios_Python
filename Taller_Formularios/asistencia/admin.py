from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo','documento','correo_electronico','fecha_asistencia','hora_ingreso','hora_salida','presente')
    list_filter = ('fecha_asistencia','presente')
    search_fields = ('nombre_completo','documento','correo_electronico')
