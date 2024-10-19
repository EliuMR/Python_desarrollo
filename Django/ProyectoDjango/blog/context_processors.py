from blog.models import Category, Article
#el context processor es una función que recibe un request y devuelve un diccionario con las variables que se van a añadir al contexto de todas las plantillas.

#La función get_pages recibe un request y devuelve un diccionario con la clave pages que contiene todas las páginas visibles ordenadas por el campo order.
def get_categories(request):
    ids = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=ids).values_list('id', 'name')
    return {'categories': categories,
            'ids': ids}
