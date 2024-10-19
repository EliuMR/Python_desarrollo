from django import template

register = template.Library()

#Creando filtro

@register.filter(name='Filtro_Custom')
def Filtro_Custom(value):
    return f"<h1 style='background:green;color:white;'>Bienvenido, {value} </h1>"
