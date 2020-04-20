from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'title', 
            'developers', 
            'genres',
            'description',
            'studentIds', 
            'hasBeenApproved',
            'build', 
        ]
    #     title = models.CharField(max_length=50, unique=True)
    # studentNames = models.CharField(max_length=80)
    # genres = models.CharField(max_length=128)
    # studentIds = models.CharField(max_length=60)
    # description = models.CharField(max_length=128)
    # build = models.FileField(upload_to="games/")
    # hasBeenApproved = models.BooleanField(default=False)
    # dateCreated = models.DateField(auto_now_add=True)