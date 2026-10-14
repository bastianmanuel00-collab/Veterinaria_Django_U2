from django.contrib import admin
from .models import Cliente, Atencion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono", "saldo")
    list_filter = ("apellido",)
    search_fields = ("nombre", "apellido", "email")


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ("cliente", "mascota", "tipo_atencion", "fecha", "costo")
    list_filter = ("tipo_atencion", "fecha")
    search_fields = ("mascota", "tipo_atencion", "cliente__nombre")

