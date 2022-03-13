from django.contrib import admin
from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'glass', 'garnish', 'basesprite', 'ingredient', 'technique']
    list_display = ['name', 'glass', 'garnish', 'basesprite', 'ingredient', 'technique']

    
admin.site.register(Recipe, RecipeAdmin)
