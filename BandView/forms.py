from django import forms
from .models import Band
from .models import Venue

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        #fields = ['email', 'message']
        fields = '__all__'
