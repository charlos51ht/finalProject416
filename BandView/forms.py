from django import forms
from .models import Band, Venue

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'