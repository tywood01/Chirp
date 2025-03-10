from django.contrib import admin
from .models import Chirp, Profile, Follow, Likes

admin.site.register(Chirp)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Likes)
