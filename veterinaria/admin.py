
from django.contrib import admin
from .models import Cliente, Atencion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono", "saldo_clp")
    list_filter = ("apellido",)
    search_fields = ("nombre", "apellido", "email")

    @admin.display(description="Saldo")
    def saldo_clp(self, obj):
        return f"${obj.saldo:,.0f}".replace(",", ".")


@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ("cliente", "mascota", "tipo_atencion", "fecha", "costo_clp")
    list_filter = ("tipo_atencion", "fecha")
    search_fields = ("mascota", "tipo_atencion", "cliente__nombre")

    @admin.display(description="Costo")
    def costo_clp(self, obj):
        return f"${obj.costo:,.0f}".replace(",", ".")
