from django.db import models
from datetime import date

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50, unique=True)
    developers = models.CharField(max_length=80)
    genres = models.CharField(max_length=128)
    studentIds = models.CharField(max_length=60)
    description = models.CharField(max_length=128)
    build = models.FileField(upload_to="games/")
    hasBeenApproved = models.BooleanField(default=False)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    # ID SMALLINT(5),
    # Title VARCHAR(32),
    # Author VARCHAR(128),
    # Genre VARCHAR(32),
    # Description VARCHAR(128),
    # Tags VARCHAR(128),
    # ReleaseDate DATE,
    # Platform VARCHAR(32),
    # Image VARCHAR(32768),
    # Link VARCHAR(32768)
