from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Band, Venue, UserType
from .forms import BandForm, VenueForm, UserRegistrationForm

# Create your views here.
def welcome(request):
    user = request.user
    context = {'user_signed_in': user.is_authenticated,
               'user_name': user.username}
    return render(request, 'welcome.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            UserType.objects.create(user=user, user_type=user_type)
            login(request, user)
            return redirect('welcome')
    else:
        form = UserRegistrationForm()
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

def updateBand(request, band_id):
    band = Band.objects.get(pk=band_id)
    form = BandForm(request.POST or None, instance=band)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('bands')
    context = {'form':form}
    return render(request, 'updateBand.html', context)

def deleteBand(request, band_id):
    band = Band.objects.get(pk=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('bands')
    else:
        context = {'band': band}
        return render(request, 'deleteBand.html', context)

def updateVenue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('venues')
    context = {'form': form}
    return render(request, 'updateVenue.html', context)

def deleteVenue(request, venue_id):
    venue = Band.objects.get(pk=venue_id)
    if request.method == 'POST':
        venue.delete()
        return redirect('venues')
    else:
        context = {'venue': venue}
        return render(request, 'deleteVenue.html', context)

def signout(request):
    logout(request)
    return redirect('welcome')
