from django.shortcuts import render
from .models import Recipe



def list(request):
    cocktail_list=Recipe.objects.order_by('pk')
    context = {'cocktail_list':cocktail_list}
    return render(request, "list.html", context)

def recipes(request,cocktail_id):
    recipe=Recipe.objects.get(id=cocktail_id)
    context = {'recipe': recipe}
    return render(request, "recipes.html", context)



def basesprite(request):
    base_list=Recipe.objects.order_by('basesprite').values('basesprite').distinct()
    context = {'base_list': base_list}
    return render(request, "basesprite.html", context)

def listbybase(request,base_name):
    lbyb=Recipe.objects.filter(basesprite=base_name)
    context = {'lbyb': lbyb}
    return render(request, "listbybase.html", context)

# Create your views here.

