from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('sign-in/', views.signin, name="sign-in"),
]