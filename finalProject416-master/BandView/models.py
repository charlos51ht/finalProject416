import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import time
# Create your models here.

class Band(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bandName = models.CharField(max_length=100, blank=False)
    bandDescription = models.TextField()
    email = models.EmailField(max_length=254, blank=False)
    phone = models.IntegerField()
    link = models.CharField(max_length=100)
    genre = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.bandName

class Venue(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    venueName = models.CharField(max_length=100, blank=False)
    venueDescription = models.TextField()
    address = models.CharField(max_length=200, blank=False)
    venueEmail = models.EmailField(max_length=254, blank=False)
    venuePhone = models.IntegerField(blank=False)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.venueName

# class Post(models.Model):
#     post_id = models.IntegerField(primary_key=True)
#     band = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Band")
#     venue = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Venue")
#     media = models.FileField()
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=150)

TYPE_CHOICES = (
    ('Band', 'Band'),
    ('Venue', 'Venue')
)

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=5, blank=False, choices=TYPE_CHOICES)

class Event(models.Model):
    event_band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event_venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    @property
    def has_happened(self):
        return date.today() > self.date

