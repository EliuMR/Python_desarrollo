from pages.models import Page

#La función get_pages recibe un request y devuelve un diccionario con la clave pages que contiene todas las páginas visibles ordenadas por el campo order.
def get_pages(request):
    
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {'pages': pages}
