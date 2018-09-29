from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_sale = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
