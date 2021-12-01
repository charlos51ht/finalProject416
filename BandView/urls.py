from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('sign-in/', views.signin, name="sign-in"),
    path('band-sign-up/', views.bandsignup, name="band-sign-up"),
    path('logout/', views.logout_user, name="logout_user")
]