from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Band
from .forms import BandForm

# Create your views here.
def welcome(request):
    user = request.user
    context = {'user_signed_in': user.is_authenticated,
               'user_name': user.username}
    return render(request, 'welcome.html', context)

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
        # get the user info from the form data and log in the user
            form.save()
            return redirect('welcome')
    else:
        form = BandForm
    return render(request, 'BandSignUp.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('welcome')
