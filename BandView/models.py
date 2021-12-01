from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genre(models.Model):
    genre = models.CharField(choices="Jazz,Funk,HipHop,Rock,Alt")

class Band(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bandName = models.CharField(max_length=100)
    bandDescription = models.CharField(max_length=100)
    profilePic = models.ImageField(blank=True)
    genre = models.ManyToManyField(Genre)

class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venueName = models.CharField(max_length=100)
    venueDescription = models.CharField(max_length=100)
    profilePic = models.ImageField(blank=True)

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    band = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.FileField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
