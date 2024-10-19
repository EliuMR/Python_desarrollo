from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login') # Decorador para requerir que el usuario este logueado
def article_list(request):
    articles = Article.objects.all() # Get all articles
    paginator = Paginator(articles, 1) # Show 2 articles per page.
    page_number = request.GET.get('page') # Get the page number
    page_articles = paginator.get_page(page_number) # Get the articles for the page number

    return render(request, 'articles/article_list.html',
                  {'title': 'List of articles',
                      'articles': page_articles})

@login_required(login_url='login') # Decorador para requerir que el usuario este logueado
def category(request, category_id):
    category = get_object_or_404(Category,id=category_id)
    articles = Article.objects.filter(categories=category)   
    return render(request, 'categories/category.html',
                  {'category': category
                   ,'articles': articles}
                  )
@login_required(login_url='login') # Decorador para requerir que el usuario este logueado
def detail(request, article_id):
    article = get_object_or_404(Article,id=article_id)
    return render(request, 'articles/detail.html',
                  {'article': article})

