from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Post


def index(request):
    """
    boardapp 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    # 정렬
    if so == 'recommend':
        post_list = Post.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        post_list = Post.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        post_list = Post.objects.order_by('-create_date')

    # 조회
    # post_list = Post.objects.order_by('-create_date')
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    # 페이징 처리
    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'boardapp/post_list.html', context)


def detail(request, post_id):
    """
    boardapp 내용 출력

    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'boardapp/post_detail.html', context)
