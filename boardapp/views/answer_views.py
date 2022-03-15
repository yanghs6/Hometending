from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Post, Answer

@login_required(login_url='account:login')
def answer_create(request, post_id):
    """
    boardapp 답변 등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('boardapp:detail', post_id=post.id), answer.id))
        else:
            form = AnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'boardapp/post_detail.html', context)


@login_required(login_url='account:login')
def answer_modify(request, answer_id):
    """
    boardapp 답변 수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('boardapp:detail', post_id=answer.post.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('boardapp:detail', post_id=answer.post.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer' : answer, 'form': form}
    return render(request, 'boardapp/answer_form.html', context)

@login_required(login_url='account:login')
def answer_delete(request, answer_id):
    """
    boardapp 답변 삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('boardapp:detail', post_id=answer.post.id)
