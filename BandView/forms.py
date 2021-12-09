from django import forms
from .models import Band, Venue,Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        exclude = ["user"]

        # widgets = {
        #     'bandName': forms.TextInput(attrs={'class': 'form-control'}),
        #     'bandDescription': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailField(attrs={'class': 'form-control'}),
        #     'phone': forms.IntegerField(attrs={'class': 'form-control'}),
        #     'link': forms.TextInput(attrs={'class': 'form-control'}),
        #     'genre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'location': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        exclude = ["user"]

        # widgets = {
        #     'venueName': forms.TextInput(attrs={'class': 'form-control'}),
        #     'venueDescription': forms.TextInput(attrs={'class': 'form-control'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'venueEmail': forms.EmailField(attrs={'class': 'form-control'}),
        #     'venuePhone': forms.IntegerField(attrs={'class': 'form-control'}),
        #     'website': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class UserRegistrationForm(UserCreationForm):
    TYPE_CHOICES = (
        ('Band', 'Band'),
        ('Venue', 'Venue')
    )
    type_user = forms.ChoiceField(choices=TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'type_user', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ["event_venue"]
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput()
        }