from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    context = {'user_signed_in': False}
    return render(request, 'welcome.html', context)

def signin(request):
    return render(request, "sign-in.html")

def bandsignup(request):
    return render(request, 'bandsignup.html')
