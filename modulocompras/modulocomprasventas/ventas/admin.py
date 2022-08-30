from django.contrib import admin
from ventas.models import Cliente, Producto

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut','nombres', 'apellidos','telefono')
    search_fields = ['nombres']
    readonly_fields = ( 'create', 'update')
    filter_horizontal = ()
    list_filter= ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)   
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','cantidad', 'costo',)
    search_fields = ['descipcion']
    readonly_fields = ( 'create', 'update')
    filter_horizontal = ()
    list_filter= ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)       
