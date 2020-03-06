from django.db import models
from datetime import date

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    studentNames = models.CharField(max_length=80) #comma seperated
    studentIds = models.CharField(max_length=60) #comma seperated
    build = models.FileField(upload_to="games/")
    hasBeenApproved = models.BooleanField(default=False)
    dateCreated = models.DateField(auto_now_add=True)
