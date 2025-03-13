"""
models.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Define the models for the chirper app.

"""

from django.contrib.auth.models import User
from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=255)
    date = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(
        "chirper.Chirp", on_delete=models.CASCADE, blank=True, null=True
    )


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.CharField(max_length=255)
    public = models.BooleanField(default=True)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("user", "chirp")


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    class Meta:
        unique_together = ("follower", "followed")
