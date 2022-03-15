from django.contrib import admin
from .models import Cocktail


# Register your models here.
class CocktailAdmin(admin.ModelAdmin):
    search_fields = ['name', 'glass', 'garnish', 'basesprite', 'recipe', 'technique']
    list_display = ['name', 'glass', 'garnish', 'basesprite', 'recipe', 'technique']

    
admin.site.register(Cocktail, CocktailAdmin)
