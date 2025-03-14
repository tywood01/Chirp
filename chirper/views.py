"""
views.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Provide view responses for the chirper app.

"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from chirper.models import Chirp, Profile, Likes, Follow
from django.urls import reverse
from chirper.forms.forms import ChirpForm, ProfileForm
from django.http import HttpResponse


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


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request, request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return HttpResponseRedirect(reverse("chirper:my_profile"))

    else:
        form = ProfileForm(request)

    return render(request, "chirper/update_profile.html", {"form": form})


def chirps(request):
    template_name = "chirper/index.html"
    chirp_list = Chirp.objects.all().order_by("-date")

    context = {
        "chirp_list": chirp_list,
        "chirp_likes": {chirp.id: chirp.likes.count() for chirp in chirp_list},
    }

    return render(request, template_name, context)


@login_required
def add_chirp(request, parent_id=None):
    if request.method == "POST":
        form = ChirpForm(request, request.POST)

        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user

            if parent_id:
                chirp.parent_id = parent_id

            form.save()
            return HttpResponseRedirect(reverse("chirper:chirps"))

    else:
        form = ChirpForm(request, initial={"parent": parent_id})

    # If GET request or form invalid, show the form
    return render(request, "chirper/create_chirp.html", {"form": form})


@login_required
def toggle_like(request, chirp_id):
    chirp = get_object_or_404(Chirp, id=chirp_id)
    like, created = Likes.objects.get_or_create(user=request.user, chirp=chirp)

    if not created:
        like.delete()

    # Fetch updated like count from the Likes model
    like_count = Likes.objects.filter(chirp=chirp).count()

    return HttpResponse(f'''
        <button 
            hx-post="{request.path}" 
            hx-swap="outerHTML"
            class="like-button">
            👍 {like_count}
        </button>
    ''')


@login_required
def toggle_follow(request, followed):
    user = get_object_or_404(User, username=followed)
    follow, created = Follow.objects.get_or_create(follower=request.user, followed=user)

    if not created:
        follow.delete()

    return redirect(reverse("chirper:chirps"))  # Or redirect to profile
