from django.urls import path
# Importar las vistas de la aplicación, se le coloca . porque se encuentran en la misma carpeta
from mainapp import views
# otra forma de importar las vistas
# from app1 import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'), # Ruta de la vista index
    path('', views.index, name='index'), # Ruta de la vista index
    path('registro/', views.register_page, name='registro'), # Ruta de la vista register_page
    path('login/', views.login_page, name='login'), # Ruta de la vista login_page
    path('logout/', views.logout_user, name='logout'), # Ruta de la vista logout_user
    ]

