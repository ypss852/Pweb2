from django.contrib import admin
from .models import Producto, Venta, Compra
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Producto)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'precio_unitario', 'total', 'fecha_venta')
    search_fields = ('cliente', 'producto__nombre')
    list_filter = ('fecha_venta',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'cantidad', 'fecha_compra')
    search_fields = ('usuario__username', 'producto__nombre')
    list_filter = ('fecha_compra',)