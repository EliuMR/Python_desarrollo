from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100,verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    slug = models.CharField(max_length=150,verbose_name='URL',unique=True) # URL amigable, unica
    visible = models.BooleanField(default=True,verbose_name='Visible') # Visible en la web
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el') # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Actualizado el') # Fecha de actualización
    order = models.IntegerField(verbose_name='Orden',default=0) # Orden de las páginas
    class Meta: #Sirve para darle un nombre en plural a la tabla
        verbose_name = 'Página' # Nombre en singular de la tabla
        verbose_name_plural = 'Páginas' # Nombre en plural de la tabla
    
    def __str__(self): # Metodo que devuelve el titulo de la página
        return self.title
