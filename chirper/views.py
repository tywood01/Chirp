# from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from chirper.models import Chirp, Profile
from chirper.templates import chirper
# Create your views here.


""" class IndexView(generic.ListView):
    template_name = "chirper/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Chirp.objects.order_by("-date")[:5]
 """


class ProfileView(generic.TemplateView):
    template_name = "chirper/profile.html"

    def get_profile(self):
        return Profile.objects()


def profile(request):
    template_name = "chirper/profile.html"
    context = {
        "profile": Profile.objects.all(),
    }
    return render(request, template_name, context)


def chirps(request):
    template_name = "chirper/index.html"
    chirp_list = Chirp.objects.all()
    context = {
        "chirp_list": chirp_list,
    }
    return render(request, template_name, context)
