from django.contrib import admin
from .models import Cocktail


class CocktailAdmin(admin.ModelAdmin):
    """
    모델 Recipe의 admin
    
    Attributes:
        search_fields: name, glass, garnish, basesprite, recipe, technique
        list_display: name, glass, garnish, basesprite, recipe, technique
    """

    search_fields = ['name', 'glass', 'garnish', 'basesprite', 'recipe', 'technique']
    list_display = ['name', 'glass', 'garnish', 'basesprite', 'recipe', 'technique']

    
admin.site.register(Cocktail, CocktailAdmin)
