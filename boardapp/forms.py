from django import forms
from boardapp.models import Post, Answer, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'imgfile']
        labels = {
            'subject': '제목',
            'content': '내용',
            'imgfile': '사진',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
