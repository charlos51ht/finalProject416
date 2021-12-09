from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Band, Venue, UserType, Event
from .forms import BandForm, VenueForm, UserRegistrationForm, EventForm
from django.db.models import Count


# Create your views here.
def welcome(request):
     user = request.user
     band = None
     venue = None
     user_type = None
     events = Event.objects.all()
     if(request.user.is_authenticated ):
        #user_type = UserType.objects.get(user=request.user).user_type
        if(user_type == 'Band'):
            band = Band.objects.get(user=user)
        if (user_type == 'Venue'):
            venue = Venue.objects.get(user=user)

     context = {'user_signed_in': request.user.is_authenticated,
                'user-type':user_type,
                'band': band,
                'venue': venue,
                'events': events}
     return render(request, 'welcome.html',context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['type_user']
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

def signup(request):
    if request.user.is_authenticated:
        user = UserType.objects.get(user_id=request.user.id)
        if (user.user_type == 'Band' and Band.objects.filter(user=request.user).count() == 0) or (
                user.user_type == 'Venue' and Venue.objects.filter(user=request.user).count() == 0):
            redirect_page = "venues"
            if user.user_type == 'Band':
                form = BandForm(request.POST or None)
                redirect_page = "bands"
            elif user.user_type == 'Venue':
                form = VenueForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    #band = form.save(commit=False)
                    form.instance.user = request.user
                    form.save()
                    return redirect(redirect_page)
            return render(request, 'SignUp.html', {'form': form})
        else:
            return redirect('welcome')
    else:
        return redirect('notauthenticated')


def not_authenticated(request):
    return render(request, 'not_authenticated.html')


#  def bandsignup(request):
#      if request.method == 'POST':
#         form = BandForm(request.POST or None)
#         if form.is_valid():
#             band = form.save(commit=False)
#             band.user = request.user
#             form.save()
#             return redirect('bands')
#         else:
#             return HttpResponse("Form is not valid")
#     else:
#         form = BandForm
#         return render(request, 'BandSignUp.html', {'form': form})
#
#
# def venuesignup(request):
#     if request.method == 'POST':
#         form = VenueForm(request.POST or None)
#         if form.is_valid():
#             venue = form.save(commit=False)
#             venue.user = request.user
#             form.save()
#             return redirect('venues')
#         else:
#             return HttpResponse("Form is not valid")
#     else:
#         form = VenueForm
#         return render(request, 'AddVenue.html', {'form': form})


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
    if request.user.is_authenticated:
        band = Band.objects.get(pk=band_id)
        if request.user.id == band.user.id:
            form = BandForm(request.POST or None, instance=band)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return redirect('bands')
            context = {'form': form}
            return render(request, 'updateBand.html', context)
        else:
            return HttpResponse("Permission denied")
    else:
        return redirect('notauthenticated')


def deleteBand(request, band_id):
    if request.user.is_authenticated:
        band = Band.objects.get(pk=band_id)
        if request.user.id == band.user.id:
            if request.method == 'POST':
                band.delete()
                return redirect('bands')
            else:
                context = {'band': band}
                return render(request, 'deleteBand.html', context)
        else:
            return HttpResponse("Permission denied")
    else:
        return redirect('notauthenticated')


def updateVenue(request, venue_id):
    if request.user.is_authenticated:
        venue = Venue.objects.get(pk=venue_id)
        if request.user.id == venue.user.id:
            form = VenueForm(request.POST or None, instance=venue)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
                    return redirect('venues')
            context = {'form': form}
            return render(request, 'updateVenue.html', context)
        else:
            return HttpResponse("Permission denied")
    else:
        return redirect('notauthenticated')


def deleteVenue(request, venue_id):
    if request.user.is_authenticated:
        venue = Band.objects.get(pk=venue_id)
        if request.user.id == venue.user.id:
            if request.method == 'POST':
                venue.delete()
                return redirect('venues')
            else:
                context = {'venue': venue}
                return render(request, 'deleteVenue.html', context)
        else:
            return HttpResponse("Permission denied")
    else:
        return redirect('notauthenticated')

def createEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_venue = Venue.objects.get(user=request.user)
            form.save()
            return redirect('welcome')
        else:
            return HttpResponse("Form is not valid")
    else:
        form = EventForm
        return render(request, 'BandSignUp.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('welcome')
