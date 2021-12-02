from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Band(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bandName = models.CharField(max_length=100, blank=False)
    bandDescription = models.TextField()
    email = models.EmailField(max_length=254, blank=False)
    phone = models.IntegerField(max_length=10)
    link = models.CharField(max_length=100)
    genre = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=100, blank=False)
    profilePic = models.ImageField(blank=False)

class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venueName = models.CharField(max_length=100, blank=False)
    venueDescription = models.TextField()
    address = models.TextField(blank=False)
    venueEmail = models.EmailField(max_length=254, blank=False)
    venuePhone = models.IntegerField(max_length=10, blank=False)
    website = models.TextField()
    profilePic = models.ImageField(blank=True)

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    band = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Band")
    venue = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Venue")
    media = models.FileField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
