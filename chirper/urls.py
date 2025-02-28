from django.urls import path
from .views import chirps
from . import views

app_name = "chirper"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("profile/<str:handle>/", views.ProfileView.as_view(), name="profile"),
    path("viewchirps", chirps, name="chirps"),
]
