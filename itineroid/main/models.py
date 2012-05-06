import datetime

from django.db import models
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
      unique=True,
      verbose_name=_('user'),
      related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'), max_length=5)


# Create your models here.
