import datetime

from django.db import models
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
  user = models.OneToOneField(User,
    unique=True,
    verbose_name=('user'),
    related_name='my_profile')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Itinerary(models.Model):
  users = models.ManyToManyField(UserProfile)
  name = models.CharField(max_length=200)
  created_on = models.DateTimeField(default=datetime.datetime.now)
  start_date = models.DateField()
  end_date = models.DateField()

class Location(models.Model):
  itinerary = models.ForeignKey(Itinerary)
  name = models.CharField(max_length=200)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

class Activity(models.Model):
  itinerary = models.ForeignKey(Location)
  name = models.CharField(max_length=200)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

  
