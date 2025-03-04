# from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from chirper.models import Chirp, Profile
from chirper.templates import chirper
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


""" class IndexView(generic.ListView):
    template_name = "chirper/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Chirp.objects.order_by("-date")[:5]
 """


def profile(request, username):
    template_name = "chirper/profile.html"
    user = get_object_or_404(User, username=username)

    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={"bio": "Default bio"},
    )
    chirps = Chirp.objects.filter(user=user).order_by("-date")
    print("Chirps found:", chirps.count())
    context = {
        "profile": profile,
        "user_chirp_list": chirps,
        "user": user,
    }
    return render(request, template_name, context)


def my_profile(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    return profile(request, username=request.user.username)


def chirps(request):
    template_name = "chirper/index.html"
    chirp_list = Chirp.objects.all()
    context = {
        "chirp_list": chirp_list,
    }
    return render(request, template_name, context)


@login_required
def add_chirp(request):
    if request.method == "POST":
        body = request.POST.get("body", "").strip()
        if body and len(body) <= 255:
            chirp = Chirp.objects.create(body=body, user=request.user)
            return HttpResponseRedirect(reverse("chirper:chirps"))
    # If GET request or form invalid, show the form
    return render(request, "chirper/add_chirp.html")
