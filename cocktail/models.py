from django.db import models

class Cocktail(models.Model):
    name=models.CharField(max_length=50)
    glass=models.CharField(max_length=50)
    garnish=models.CharField(max_length=50)
    basesprite=models.CharField(max_length=50)
    recipe=models.TextField()
    technique=models.CharField(max_length=50)
    def __str__(self):
        return f"id={self.id},glass={self.glass}, garnish={self. garnish},basesprite={self.basesprite},ingredient={self.ingredient},technique={self.technique}"


# Create your models here.
