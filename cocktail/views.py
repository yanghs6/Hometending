from django.shortcuts import render
from .models import Recipe
from django.db.models import Q


def list(request):
    # 조회
    cocktail_alllist = Recipe.objects.order_by('pk')
    kw = request.GET.get('kw', '')  # 검색어
    # 검색
    if kw:
        cocktail_alllist = cocktail_alllist.filter(
            Q(name__icontains=kw) |  # 이름검색
            Q(basesprite__icontains=kw) |  # 베이스검색
            Q(ingredient__icontains=kw) |  # 재료검색
            Q(garnish__icontains=kw)  #가니시검색
        ).distinct()
    n=4
    cocktail_list = [cocktail_alllist[i * n:(i + 1) * n] for i in range((len(cocktail_alllist) + n - 1) // n)]
    context = {'cocktail_alllist':cocktail_alllist,'cocktail_list':cocktail_list, 'kw': kw}
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

