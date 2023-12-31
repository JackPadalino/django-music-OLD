from django import forms
from django.apps import apps
from .models import Artist,Track

#~~~~~Project model forms~~~~~#
class UploadTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['artist','title','genre','file']
        artist = forms.ModelChoiceField(queryset=Artist.objects.all(), empty_label="-")