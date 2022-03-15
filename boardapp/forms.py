from django import forms
from boardapp.models import Post, Answer, Comment


class PostForm(forms.ModelForm):
    """
    모델 Post의 Form
    
    class Meta:
        model: Post
        fields: subject, content, imgfile
    """
    class Meta:
        model = Post
        fields = ['subject', 'content', 'imgfile']
        labels = {
            'subject': '제목',
            'content': '내용',
            'imgfile': '사진',
        }


class AnswerForm(forms.ModelForm):
    """
    모델 Answer의 Form
    
    class Meta:
        model: Answer
        fields: content
    """
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    """
    모델 Comment의 Form
    
    class Meta:
        model: Comment
        fields: content
    """
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
