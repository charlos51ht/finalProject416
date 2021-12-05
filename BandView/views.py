from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Band, Venue
from .forms import BandForm, VenueForm, UserRegistrationForm

# Create your views here.
def welcome(request):
    user = request.user
    context = {'user_signed_in': user.is_authenticated,
               'user_name': user.username}
    return render(request, 'welcome.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'Registration.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get the user info from the form data and log in the user
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})

def bandsignup(request):
    if request.method == 'POST':
        form = BandForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('bands')
    else:
        form = BandForm
        return render(request, 'BandSignUp.html', {'form': form})

def venuesignup(request):
    if request.method == 'POST':
        form = VenueForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('venues')
    else:
        form = VenueForm
        return render(request, 'AddVenue.html', {'form': form})

def bands(request):
    bands = Band.objects.all()
    return render(request, 'Bands.html', {'bands': bands})

def venues(request):
    venues = Venue.objects.all()
    return render(request, 'Venues.html', {'venues': venues})

def bandprofile(request, band_id):
    b = Band.objects.get(pk=band_id)
    context = {'band': b}
    return render(request, 'BandProfile.html', context)


def venueprofile(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    context = {'venue': venue}
    return render(request, 'VenueProfile.html', context)

def signout(request):
    logout(request)
    return redirect('welcome')
