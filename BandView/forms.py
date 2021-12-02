from django import forms
from .models import Band, Venue

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['bandName', 'bandDescription', 'email', 'phone', 'link', 'genre', 'location', 'profilePic']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venueName', 'venueDescription', 'venueEmail', 'venuePhone', 'address', 'website', 'profilePic']