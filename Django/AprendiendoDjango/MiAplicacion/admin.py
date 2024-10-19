from django.contrib import admin #permite hacer configuraciones en el panel de administracion

from .models import *
# Register your models here.

#Registramos los modelos para que aparezcan en el panel de administracion
class ArticleAdmin(admin.ModelAdmin): #Clase para personalizar el panel de administracion
    readonly_fields = ('created_at','updated_at') #Campos que no se pueden modificar

admin.site.register(Article,ArticleAdmin) #Registramos el modelo Article y le pasamos la clase ArticleAdmin para personalizar el panel de administracion
admin.site.register(Category)

#cambiar el titulo de panel
admin.site.site_header = "Panel de Mi Aplicación"
#cambiar el subtitulo de panel
admin.site.site_title = "Panel de Mi Aplicación"
#cambiar el titulo de la pagina de administracion
admin.site.index_title = "Panel de gestión"



