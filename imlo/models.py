from django.db import models

# Create your models here.
from config import settings


class TextLatin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user.username
    