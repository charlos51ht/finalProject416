from django import forms
from .models import Band, Venue
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    TYPE_CHOICES = (
        ('Band', 'Band'),
        ('Venue', 'Venue')
    )
    type_user = forms.ChoiceField(choices=TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'type_user', 'password1', 'password2']

