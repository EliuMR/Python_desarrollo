"""
URL configuration for AprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiAplicacion import views #importando los métodos de mi aplicación

#Aquí tomando nuestro domino vamos a agregar subrutas, el método deseado a ejecutar con dicha subruta y un nombre
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Primera-funcion/', views.primera_Funcion, name="PrimeraFuncion"),
    path('',views.index,name="Index"), #Cuando no damos ninguna ruta es la de inicio
    path('inicio/',views.index,name="Index 1"),
    
    path('pagina/', views.pagina, name="Pagina"),
    path('pagina/<int:redirigir>', views.pagina, name="Pagina"),
    
    path('contacto/<str:nombre_parametro>',views.contacto, name="contacto"), #Pasar parametro del tipo que uno quiera, para pasar parametros al metodo
    
    path('contacto_po/',views.contacto_po, name="contacto_po"), #Pasar parametros opcionales hay que colocar las opciones, es decir con y sin parametros
    path('contacto_po/<str:nombre_parametro>',views.contacto_po, name="contacto_po"), #Pasar parametro del tipo que uno quiera, para pasar parametros al metodo
    path('contacto_po/<str:nombre_parametro>/<str:apellido_parametro>',views.contacto_po, name="contacto_po"), #Pasar parametro del tipo que uno quiera, para pasar parametros al metodo
    
    path('crear_articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name="crear_articulo"), 
    path('select_articulo/<int:id>',views.select_articulo, name="select_articulo"), 
    path('editar_articulo/<int:id>/<str:title>/<str:content>/<str:public>',views.editar_articulo, name="editar_articulo"), #
    path('select_all_articles/',views.select_all_articles, name="select_all_articles"), #Seleccionar todos los articulos"

    path('delete_article/<int:id>/',views.delete_article, name="delete_article"), #Eliminar un articulo
    path('save_article/',views.save_article, name="save_article"), #Guardar un articulo
    path('create_article/',views.create_article, name="create_article"), #Crear un articulo
    
    path('create_article_form/',views.create_article_form, name="create_article_form"), #Crear un articulo pero usando un formulario creado en forms.py en django
    ]

 #Para poder ver las imagenes que se suben al servidor
from django.conf import settings
if settings.DEBUG: #Si estamos en modo debug que significa que estamos en desarrollo modo local
    from django.conf.urls.static import static
    #El media_url es la ruta que se le asigna a las imagenes que se suben al servidor
    #El document_root es la ruta donde se guardan las imag
    #la diferencia entre media_url y media_root es que media_url es la ruta que se le asigna a las imagenes que se suben al servidor y media_root es la ruta donde se guardan las imagenes
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Agregamos la ruta de las imagenes 

