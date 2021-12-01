from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def welcome(request):
    context = {'user_signed_in': False}
    return render(request, 'welcome.html', context)

def signin(request):
    return render(request, "sign-in.html")

def bandsignup(request):
    return render(request, 'bandsignup.html')
