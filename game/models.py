from django.db import models
from django.contrib.auth.models import User

class OnlineGames(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
