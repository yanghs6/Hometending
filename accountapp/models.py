from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class HometendUser(AbstractUser):
    star = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
