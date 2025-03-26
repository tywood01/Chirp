"""
models.py

Authors: Silas Curtis, Tytus Woodburn
Emails: silas.curtis@student.cune.edu tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01 https://github.com/SilasEC

Purpose:
    Define the models for the chirper app.
    These will be mapped to the database by Django's ORM.

"""

from django.contrib.auth.models import User
from django.db import models


class Chirp(models.Model):
    """Represents a short message (chirp) in the Chirper app."""

    body = models.CharField(max_length=255)
    date = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(
        "chirper.Chirp", on_delete=models.CASCADE, blank=True, null=True
    )


class Profile(models.Model):
    """Represents a user's profile and content about them."""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.CharField(max_length=255)
    public = models.BooleanField(default=True)


class Likes(models.Model):
    """Represents a user liking a post."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "chirp"), name="unique user chirp like"
            )
        ]


class Follow(models.Model):
    """Represents a user following another user."""

    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )

    class Meta:
        """One can't follow oneself."""

        constraints = [
            models.UniqueConstraint(
                fields=("follower", "followed"), name="unique follower followed"
            )
        ]
