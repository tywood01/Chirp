from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chirp(models.Model):
    body = models.CharField(max_length=255)
    date = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey("chirper.Chirp", on_delete=models.CASCADE, null=True)


class Likes(models.Model):
    pass


class Follows(models.Model):
    pass


def add(x: int, y: int) -> int:
    return x + y
