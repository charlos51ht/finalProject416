from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('sign-in/', views.signin, name="sign-in"),
    path('register/', views.register_view, name="register"),
    path('signup/', views.signup, name="sign-up"),
    path('bandsignup/', views.bandsignup, name="band-sign-up"),
    path('venuesignup/', views.venuesignup, name="venue-sign-up"),
    path('bands/', views.bands, name="bands"),
    path('venues/', views.venues, name="venues"),
    path('bandprofile/<str:band_id>', views.bandprofile, name="band-profile"),
    path('venueprofile/<str:venue_id>', views.venueprofile, name="venue-profile"),
    path('updateband/<str:band_id>', views.updateBand, name="updateBand"),
    path('deleteband/<str:band_id>', views.deleteBand, name="deleteBand"),
    path('updatevenue/<str:venue_id>', views.updateVenue, name="updateVenue"),
    path('deletevenue/<str:venue_id>', views.deleteVenue, name="deleteVenue"),
    path('create-event/', views.createEvent, name="createEvent"),
    path('sign-out/', views.signout, name="sign-out")
]