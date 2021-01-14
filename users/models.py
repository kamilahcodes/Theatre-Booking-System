from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

     date_of_birth = models.DateField(null=True, blank=True)
     agency_name = models.BooleanField(default=False, blank=True)

    # add additional fields in here
