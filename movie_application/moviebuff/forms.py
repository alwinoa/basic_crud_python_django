from django.forms import ModelForm
from moviebuff.models import CreateMovie


class MovieForms(ModelForm):
    class Meta:
        model = CreateMovie
        fields = ['tittle','year','summary']


