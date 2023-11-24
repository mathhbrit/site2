from django.db import models

# Create your models here.

from django.conf import settings


class Personagem(models.Model):
    name = models.CharField(max_length=255)
    game_ano = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.game_ano})'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'


class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    personagens = models.ManyToManyField(Personagem)

    def __str__(self):
        return f'{self.name} by {self.author}'
    
