"""
forms.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Define reusable forms for the chirper app.

"""

from django import forms
from chirper.models import Chirp, Profile


class ChirpForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.instance.user = request.user

    class Meta:
        model = Chirp
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 60,
                    "placeholder": "What's on your mind, bird brain?",
                    "maxlength": 255,
                }
            ),
        }


class ProfileForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.instance.user = request.user

    class Meta:
        model = Profile
        fields = ["bio", "public"]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 60,
                    "placeholder": "Tell us a lil about your bird-self!",
                    "maxlength": 255,
                }
            ),
            "public": forms.CheckboxInput(),
        }
