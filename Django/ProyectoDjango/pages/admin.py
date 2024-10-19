from django.contrib import admin

# Register your models here.
from .models import *

#Configuración de la página de inicio
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # Campos de solo lectura
    search_fields = ('title', 'content') # Campos de búsqueda
    list_filter = ('visible',) # Filtros
    list_display = ('title', 'visible', 'created_at') # Campos a mostrar
    ordering = ('-created_at',) # Orden de los registros


admin.site.register(Page, PageAdmin)

#Configuración del panel de administración
title = "Panel de Administración"
subtitle = "Panel de administración de la aplicación web"
admin.site.site_header = title # Título de la página
admin.site.site_title = title # Título de la pestaña del navegador
admin.site.index_title = subtitle # Título de la página principal del panel de administración


