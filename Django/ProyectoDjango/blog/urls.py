from django.urls import path
from . import views

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('category/<int:category_id>', views.category, name='category'),
    path('article_detail/<int:article_id>', views.detail, name='detail'),
    ]


