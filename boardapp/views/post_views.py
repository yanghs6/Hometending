from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ImageField
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from PIL import Image, UnidentifiedImageError

from ..forms import PostForm
from ..models import Post


@login_required(login_url='account:login')
def post_create(request):
    """
    boardapp 질문 등록

    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            
            if 'imgfile' in request.FILES:
                post.imgfile = request.FILES["imgfile"]
            
            post.save()
            return redirect('boardapp:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'boardapp/post_form.html', context)

@login_required(login_url='account:login')
def post_modify(request, post_id):
    """
    boardapp 질문 수정
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('boardapp:detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_date = timezone.now()
            post.imgfile = request.FILES["imgfile"]
            
            # 이미지 파일 확인
            try:
                tmp_img = Image.open(post.imgfile)
                tmp_img.verify()
            except:
                message = "이미지 파일이 아닙니다. 올바른 파일을 입력해주세요."
                context = {'form': form, 'message': message}
                return render(request, 'boardapp/post_form.html', context)
            else:
                post.save()
                return redirect('boardapp:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
        
    context = {'form': form}
    return render(request, 'boardapp/post_form.html', context)

@login_required(login_url='account:login')
def post_delete(request, post_id):
    """
    boardapp 질문 삭제
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user !=post.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('boardapp:detail', post_id=post.id)
    post.delete()
    return redirect('boardapp:index')

@login_required(login_url='account:login')
def post_photo(request):
    """
    boardapp 사진 등록
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        img = request.FILES["imgfile"]
        post = Post(
            imgfile=img
        )
        post.save()
        return redirect('boardapp:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'boardapp/post_form.html', context)
