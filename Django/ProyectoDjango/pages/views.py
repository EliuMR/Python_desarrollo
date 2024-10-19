from django.shortcuts import render
from .models import Page

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login') # Decorador para requerir que el usuario este logueado
def page(request,slug):
    page = Page.objects.get(slug=slug) # Obtiene la página con el slug pasado por parámetro
    return render(request, 'pages/page.html',
                  {
                   'page': page})
