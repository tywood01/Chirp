"""
chirper/urls.py

Authors: Silas Curtis, Tytus Woodburn
Emails: silas.curtis@student.cune.edu tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Provide view responses for the chirper app.

"""

from django.urls import path
from .views import profile
from . import views

app_name = "chirper"
urlpatterns = [
    path("", views.chirps, name="chirps"),
    path("profile/<str:username>/", profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("profile/", views.my_profile, name="my_profile"),
    path("addchirp/", views.add_chirp, name="add_chirp"),
    path("add/<int:parent_id>/", views.add_chirp, name="reply_chirp"),
    path("chirp/<int:chirp_id>/like/", views.toggle_like, name="toggle_like"),
    path("toggle_follow/<str:followed>/", views.toggle_follow, name="toggle_follow"),
]
