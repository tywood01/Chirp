# from django.shortcuts import render
from django.views import generic
from chirper.models import Chirp
from chirper.templates import chirper
# Create your views here.


class IndexView(generic.ListView):
    template_name = "chirper/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Chirp.objects.order_by("-date")[:5]
