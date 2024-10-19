from django.shortcuts import render, HttpResponse,redirect

#Importamos los modelos de la aplicación para poder usarlos
from MiAplicacion.models import Article, Category

from django.db.models import Q  #Para hacer consultas más complejas

#Importamos el formulario que creamos en forms.py
from MiAplicacion.forms import FromArticle

#Sesiones flash
from django.contrib import messages
# Create your views here.
#MVC: Modelo vista controlador  -> Acciones(métodos)
#MVT: Modelo vista template     -> Acciones

#Layaout tipo meno de direcciones que se pude colocar para que se encuentre visible en todas la paginas
#Plantilla de barra de navegación
layout = """
   <h1> Sitio con Django </h1>
    <hr/>
    <ul>
    <li> <a href = "/inicio" > Inicio <a> </a> </li>
    <li> <a href="/pagina">Pagina </a> </li>
    <li> <a href="/contacto_po"> Contacto </a> </li>
    </ul>
    <hr/>
"""
 
#Todas la acciones deben agregarse a urls.py dentro del directorio del proyecto
def primera_Funcion(request): #Método
    return HttpResponse(layout+"""
                        <h1/>Primera función<h1/>
                            <p> Hola Django </p>

                        """) #
def index(request):
    """template = ""
        <h1> Página de inicio </h1>
        <p> Años hasta el 2050 :</p>
        <ul>
    ""
    
    year= 2024
    while year <=2050:
        if year%2 == 0:
            template += f"<li>{str(year)}</li>"
        year+=1
    
    template += "</ul>"
    """
    
    year = 2021
    rango = range(year,2051)

    nombre = "Eliú Moreno Ramírez"
    lista = ["item 1","item 2", "item 3"]
    return render(request,'index.html',
            #Estas son variables que se pasarán, i.e,
            #Podemos generar cierta lógica y pasarla en este tercer argumento para después
            #pasarla al html, las variables deben pasarse en forma de diccionariol
            {
                'titulo' : 'Página de inicio', 
                'variable':'Dato 1',
                'nombre' : nombre,
                'lista': lista,
                'years': rango
            }
                  )#Estamos cargando un archivo html
#
def pagina(request,redirigir=0):
    if redirigir==1:
        #Las redirecciones toman el nombre de la url no la url como tal
        return redirect('contacto_po',nombre_parametro="name",apellido_parametro="last") #Vamor a redirigir si llega un parametro deseado
    return render(request,"hola.html",
                  {'texto': '',
                   'lista': ["uno","dos","tres"]}
                  )
 
#Recojer parametros por medio de URL, pero son obligatorios o sino la ruta no existe
def contacto(request,nombre_parametro):
    return HttpResponse(layout+
        f"""
        <h1> Pagina de contacto </h1>
        <p> Hola {nombre_parametro} </p>
        """
    )

#Con parametros opcionales, hay que dar los valores por defecto
"""def contacto_po(request,nombre_parametro="",apellido_parametro=""):
    html = ""
    if nombre_parametro and apellido_parametro: #Colocamos un casp para mostrar cuando hay parametros
        html += f"<p>Hola {nombre_parametro} {apellido_parametro}</p>"
    return HttpResponse(layout+
        f{
        <h1> Pagina de contacto </h1>
        }
        +html
    
"""

def contacto_po(request):
    return render(request,"contacto.html")



#Usando las bases de datos creadas en models.py,
#utilizando los parametros que se pasan por la URL
def crear_articulo(request,title,content,public): #Esta vista se encargará de crear un articulo
    articulo = Article(
        title = title,
        contet = content,
        public = public
    )

    articulo.save() #Guardamos el articulo en la base de datos

    return HttpResponse(f"Articulo creado :<strong>{articulo.title} - {articulo.contet}</strong>")  


#Sacar un articulo de la base de datos
def select_articulo(request, id):
    try:
        articulo = Article.objects.get(id=id)
        response = f"Articulo seleccionado :<strong>{articulo.title} - {articulo.contet}</strong>"
    except:    
        response = "Articulo no encontrado"
    return HttpResponse(response)

#Editar articulo
def editar_articulo(request,id,title,content,public):
    try:
        articulo = Article.objects.get(pk=id)
        articulo.title = title
        articulo.contet = content
        articulo.public = public
        articulo.save()
        response = f"Articulo editado :<strong>{articulo.title} - {articulo.contet}</strong>"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)

def select_all_articles(request):
    #Sacar todos los articulos de la base de datos
    articulos = Article.objects.order_by('id')[:10] #Sacar los primeros 10 articulos
    #Filtros
    #articulos = Article.objects.filter(public=True, title__lookuptype="articulo") #Sacar los articulos que tengan el campo public en True y que el titulo contenga la palabra articulo
    #articulos = Article.objects.filter(id__gt=5) #Sacar los articulos que tengan un id mayor a 5
    #articulos = Article.objects.filtes(id__gte=5) #Sacar los articulos que tengan un id mayor o igual a 5
    #Mostrar aquellos que sean publicos
    articulos = Article.objects.filter(public=True)
    
    #Consulta más compleja con Q
    #articulos = Article.objects.filter(Q(public=True) | Q(title__contains="articulo")) #Consulta con or


    #Consulta en sql, pero no es muy recomendable
    #articulos = Article.objects.raw("SELECT * FROM MiAplicacion_article WHERE public = 1") #Consulta en sql
    return render(request,'articulos.html',{'articulos':articulos})

def delete_article(request,id):
    try:
        articulo = Article.objects.get(pk=id)
        articulo.delete()
        return redirect('select_all_articles')
    except:
        return HttpResponse("Articulo no encontrado")

#Esta serviria con formulario
def save_article(request):
    #Primero verificamos que recibimos un get o un post
    if request.method == 'POST':
        #Sacamos los datos del formulario
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']


        articulo = Article(
            title = title,
            contet = content,
            public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado :<strong>{articulo.title} - {articulo.contet}</strong>")  
    else:
        return HttpResponse("No se ha podido guardar el articulo")
      


def create_article(request):
    return render(request,'create_article.html')

#Crearemos un formulario para crear un articulo del archivo forms.py
def create_article_form(request):
    if request.method == 'POST':
        form = FromArticle(request.POST)
        if form.is_valid(): #Si el formulario es valido lo que significa que los datos son correctos
            data_form = form.cleaned_data #Sacamos los datos del formulario
            title = data_form.get('title')            
            content = data_form.get('content')
            public = data_form.get('public')
            #Creamos un articulo
            articulo = Article(
                title = title,
                contet = content,
                public = public
            )

            #crear un mensaje flash que solo se muestra una vez
            messages.success(request,f'Has creado el articulo correctamente : {articulo.title}')

            articulo.save()#Guardamos el articulo
            
            return redirect('select_all_articles') #Redirigimos a la vista de todos los articulos
            #return HttpResponse(articulo.title + " - " + articulo.contet+ " - " + str(articulo.public))
        else:
            return render(request,'create_article_form.html',{'form':form})
    else:
        form = FromArticle() #Creamos un formulario vacio


    form = FromArticle()
    return render(request,'create_article_form.html',{'form':form})
