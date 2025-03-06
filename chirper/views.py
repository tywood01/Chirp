# from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from chirper.models import Chirp, Profile, Likes, Follow
from chirper.templates import chirper
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


# Views
def profile(request, username):
    template_name = "chirper/profile.html"
    user = get_object_or_404(User, username=username)

    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={"bio": "Default bio"},
    )

    chirps = Chirp.objects.filter(user=user).order_by("-date")
    is_following = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user, followed=user
        ).exists()

    context = {
        "profile": profile,
        "user_chirp_list": chirps,
        "user": user,
        "is_following": is_following,
    }
    return render(request, template_name, context)


def my_profile(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")

    return profile(request, username=request.user.username)


def chirps(request):
    template_name = "chirper/index.html"
    chirp_list = Chirp.objects.all().order_by("-date")

    context = {
        "chirp_list": chirp_list,
        "chirp_likes": {chirp.id: chirp.likes.count() for chirp in chirp_list},
    }

    return render(request, template_name, context)


@login_required
def add_chirp(request):
    if request.method == "POST":
        body = request.POST.get("body", "").strip()
        if body and len(body) <= 255:
            Chirp.objects.create(body=body, user=request.user)
            return HttpResponseRedirect(reverse("chirper:chirps"))

    # If GET request or form invalid, show the form
    return render(request, "chirper/add_chirp.html")


@login_required
def toggle_like(request, chirp_id):
    chirp = get_object_or_404(Chirp, id=chirp_id)
    like, created = Likes.objects.get_or_create(user=request.user, chirp=chirp)

    # If like already exists, remove it
    if not created:
        like.delete()

    # Redirect back to chirps
    return redirect(reverse("chirper:chirps"))


@login_required
def toggle_follow(request, followed):
    user = get_object_or_404(User, username=followed)
    follow, created = Follow.objects.get_or_create(follower=request.user, followed=user)

    if not created:
        follow.delete()

    return redirect(reverse("chirper:chirps"))  # Or redirect to profile
