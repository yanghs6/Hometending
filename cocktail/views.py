from django.shortcuts import render
from .models import Cocktail
from django.db.models import Q


def list(request):
    """
    칵테일 리스트
    """
    # 조회
    cocktail_alllist = Cocktail.objects.order_by('pk')
    kw = request.GET.get('kw', '')  # 검색어
    # 검색
    if kw:
        cocktail_alllist = cocktail_alllist.filter(
            Q(name__icontains=kw) |  # 이름검색
            Q(basesprite__icontains=kw) |  # 베이스검색
            Q(recipe__icontains=kw) |  # 재료검색
            Q(garnish__icontains=kw)  #가니시검색
        ).distinct()
    n=4
    cocktail_list = [cocktail_alllist[i * n:(i + 1) * n] for i in range((len(cocktail_alllist) + n - 1) // n)]
    context = {'cocktail_list':cocktail_list, 'kw': kw}
    return render(request, "cocktail/list.html", context)

def cocktails(request,cocktail_id):
    """
    칵테일 상세보기
    """
    cocktail=Cocktail.objects.get(id=cocktail_id)
    context = {'cocktail': cocktail}
    return render(request, "cocktail/cocktails.html", context)

def basesprite(request):
    """
    베이스별 칵테일 리스트
    """
    base_list=Cocktail.objects.order_by('basesprite').values('basesprite').distinct()
    context = {'base_list': base_list}
    return render(request, "cocktail/basesprite.html", context)

def listbybase(request,base_name):
    """
    베이스 선택 후 칵테일 리스트
    """
    lbyb=Cocktail.objects.filter(basesprite=base_name)
    context = {'lbyb': lbyb,'base_name':base_name}
    return render(request, "cocktail/listbybase.html", context)
