from django. shortcuts import render
from .forms import QuestionForm
from .models import Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def index(request):
    """
    boardapp 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'boardapp/question_list.html', context)

def detail(request, question_id):
    """
    boardapp 내용 출력

    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'boardapp/question_detail.html', context)

def answer_create(request, question_id):
    """
    boardapp 답변 등록

    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())

    return redirect('boardapp:detail', question_id=question.id)

def question_create(request):
    """
    boardapp 질문 등록

    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('boardapp:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'boardapp/question_form.html', context)