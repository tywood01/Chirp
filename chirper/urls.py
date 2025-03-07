from django.urls import path
from .views import profile
from . import views

app_name = "chirper"
urlpatterns = [
    path("profile/<str:username>/", profile, name="profile"),
    path("profile/", views.my_profile, name="my_profile"),
    path("addchirp/", views.add_chirp, name="add_chirp"),
    path("add/<int:parent_id>/", views.add_chirp, name="reply_chirp"),
    path("", views.chirps, name="chirps"),
    path("chirp/<int:chirp_id>/like/", views.toggle_like, name="toggle_like"),
    path("toggle_follow/<str:followed>/", views.toggle_follow, name="toggle_follow"),
]
