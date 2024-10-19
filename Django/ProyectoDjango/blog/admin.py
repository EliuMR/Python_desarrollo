from django.contrib import admin
from .models import Category, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()
#Registramos los modelos para que se puedan administrar desde el panel de administración
#Se agregan dos, uno para especificar que se va a administrar y otro para especificar que se va a mostrar
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

