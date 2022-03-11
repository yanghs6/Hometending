from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='account:login')
def question_create(request):
    """
    boardapp 질문 등록

    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.imgfile = request.FILES["imgfile"]
            question.save()
            return redirect('boardapp:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'boardapp/question_form.html', context)

@login_required(login_url='account:login')
def question_modify(request, question_id):
    """
    boardapp 질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('boardapp:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('boardapp:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'boardapp/question_form.html', context)

@login_required(login_url='account:login')
def question_delete(request, question_id):
    """
    boardapp 질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user !=question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('boardapp:detail', question_id=question.id)
    question.delete()
    return redirect('boardapp:index')

@login_required(login_url='account:login')
def question_photo(request):
    """
    boardapp 사진 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        img = request.FILES["imgfile"]
        question = Question(
            imgfile=img
        )
        question.save()
        return redirect('boardapp:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'boardapp/question_form.html', context)