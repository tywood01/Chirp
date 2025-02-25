from django.contrib.auth.models import User
from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=255)
    date = models.DateTimeField("Created At", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey("chirper.Chirp", on_delete=models.CASCADE, null=True)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        # Ensures only one like per user per chirp
        unique_together = ("user", "chirp")


""" class Follows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    ) """

