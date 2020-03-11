from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    listOfStudents = models.CharField(max_length=150, blank=True)