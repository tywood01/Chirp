from django import forms
from chirps.models import Chirp


class ChirpForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = request.user

    class Meta:
        model = Chirp
        fields = ["body"]
