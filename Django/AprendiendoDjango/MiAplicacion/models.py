from django.db import models


"""
En Django, un modelo es una clase que representa una tabla en la base
de datos. Los modelos se definen en el archivo models.py de una 
aplicación y permiten interactuar con la base de datos de una manera 
orientada a objetos. Cada atributo de la clase representa una columna 
en la tabla de la base de datos.
"""
# Create your models here.

#modelo Articulo
class Article(models.Model): #Indicamos que esto es un modelo
    #Campos
    title       = models.CharField(max_length = 100,verbose_name = 'Titulo') #varchar(100)
    contet      = models.TextField(verbose_name = 'Contenido') #text
    public      = models.BooleanField(verbose_name = '¿Publicado?') #boolean
    image       = models.ImageField(blank=True,null=True,verbose_name = 'Imagen', upload_to = 'articles') #imagen, se va a guardar en la carpeta articles que esta en la raiz del proyecto en media
    created_at  = models.DateTimeField(auto_now_add = True,verbose_name = 'Creado') #cuando crea el articulo por primera vez
    updated_at  = models.DateTimeField(auto_now = True,verbose_name = 'Editado') #cuando se actualiza el articulo
    #Metadatos, con estos no hay que hacer migraciones
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        #por fecha de creacion de manera descendente
        ordering = ['created_at']
    
    #Metodo para mostrar el titulo del articulo en el panel de administracion
    def __str__(self):
        if self.public:
            public = "publico"
        else:
            public = "privado"
        return f"{self.title} {public}"

#modelo Categoria
class Category(models.Model):
    name        = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    created_at  = models.DateTimeField()
    #Metadatos, con estos no hay que hacer migraciones
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created_at']

