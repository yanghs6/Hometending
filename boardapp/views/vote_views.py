from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Post, Answer


@login_required(login_url='account:login')
def vote_post(request, post_id):
    """
    질문추천등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
    return redirect('boardapp:detail', post_id=post.id)


@login_required(login_url='account:login')
def vote_answer(request, answer_id):
    """
    답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('boardapp:detail', post_id=answer.post.id)
