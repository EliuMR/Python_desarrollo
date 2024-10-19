from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User #Importamos el modelo de usuario de django
# Create your models here.

#Modelos de categorias y de articulos
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self): #Para que se muestre el nombre de la categoria en el panel de administración
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles/")
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")
    user = models.ForeignKey(User, editable=False,verbose_name="Usuario", on_delete=models.CASCADE) #Usuario que crea el articulo, relacion uno a muchos con el modelo User, con la propiedad CASCADE si se elimina un usuario se eliminan todos sus articulos

    #Relación de muchos a muchos, un articulo puede tener muchas categorias y una categoria puede tener muchos articulos
    categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True)
    
    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
    
    def __str__(self): #Para que se muestre el nombre del articulo en el panel de administración
        return self.title
