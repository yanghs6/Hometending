from django.db import models
from accountapp.models import HometendUser



class Registration(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    # phone = models.BigIntegerField(max_length=10,primary_key=True)
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


class Question(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE,
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE,
                               related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # voter = models.ManyToManyField(User, related_name='voter_question')
    voter = models.ManyToManyField(HometendUser, related_name='voter_question')
    imgfile = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE,
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE,
                               related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    # voter = models.ManyToManyField(User, related_name='voter_answer')
    voter = models.ManyToManyField(HometendUser, related_name='voter_answer')


class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(HometendUser, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
