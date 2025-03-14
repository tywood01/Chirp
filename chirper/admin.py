"""
admin.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Adjust configuration for the admin interface.

"""

from django.contrib import admin
from .models import Chirp, Profile, Follow, Likes

admin.site.register(Chirp)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Likes)
