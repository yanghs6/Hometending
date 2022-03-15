from django.db import models
from accountapp.models import HometendUser



class Registration(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dob=models.DateField()
    user = models.OneToOneField(HometendUser,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.fname

class candidate(models.Model):
    full_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    total_vote = models.IntegerField(default=0)
    def __str__(self):
        return "{} -- {}".format(self.full_name,self.position)


class Post(models.Model):
    """
    게시글 모델
    
    Attributes:
        author: FK(HometendUser), 작성자
        subject: char(200), 제목
        content: text, 내용
        create_date: datetime, 작성일
        modify_date: datetime, 수정일
        voter: 다대다 테이블 생성(HometendUser), 게시글 추천인
        imgfile: varchar(100), 이미지
    """
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE,
                               related_name='author_post')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(HometendUser, related_name='voter_post')
    imgfile = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    """
    답변 모델
    
    Attributes:
        author: FK(HometendUser), 작성자
        content: text, 내용
        create_date: datetime, 작성일
        modify_date: datetime, 수정일
        voter: 다대다 테이블 생성(HometendUser), 답변 추천인
    """
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE,
                               related_name='author_answer')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(HometendUser, related_name='voter_answer')


class Comment(models.Model):
    """
    댓글 모델
    
    Attributes:
        author: FK(HometendUser), 작성자
        content: text, 내용
        create_date: datetime, 작성일
        modify_date: datetime, 수정일
        author: FK(Post), 게시글
        author: FK(Answer), 답변
    """
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
