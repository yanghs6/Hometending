from django.db import models
from django.contrib.auth.models import AbstractUser


class HometendUser(AbstractUser):
    """
    프로젝트 유저 모델
    
    AbstractBaseUser Model을 상속받아 유저 모델 재정의
    
    Attributes:
        star(int): 임시
    """
    star = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
