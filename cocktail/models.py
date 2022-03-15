from django.db import models


class Cocktail(models.Model):
    """
    칵테일 모델
    
    Attributes:
        name: char(50), 칵테일 이름
        glass: char(50), 글래스
        garnish: char(50), 가니쉬
        basespite: char(50), 베이스
        recipe: text, 레시피
        technique: char(50), 제조 기술
    """
    name = models.CharField(max_length=50)
    glass = models.CharField(max_length=50)
    garnish = models.CharField(max_length=50)
    basesprite = models.CharField(max_length=50)
    recipe = models.TextField()
    technique = models.CharField(max_length=50)
    
    def __str__(self):
        return f"id={self.id},glass={self.glass}, garnish={self. garnish},basesprite={self.basesprite},recipe={self.recipe},technique={self.technique}"
