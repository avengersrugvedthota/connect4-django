from django.db import models

class Game(models.Model):
    url = models.URLField(max_length=2048)
    image = models.ImageField(upload_to='game/images', blank=True)