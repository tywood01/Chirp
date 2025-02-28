from django.urls import path
from .views import chirps, profile
from . import views

app_name = "chirper"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
   # path("profile/<str:handle>/", profile, name="profile"),
    path("viewchirps", chirps, name="chirps"),
    path("profile/<str:username>/", profile, name="profile"),
    path("profile/", views.my_profile, name="my_profile"),
]
