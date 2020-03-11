from games.models import Game
from games.serializers import GameSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse

class GameList(mixins.CreateModelMixin, 
            mixins.ListModelMixin,
            generics.GenericAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):   
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class GameDetail(APIView):

    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        zip_file = open(serializer.data["build"], 'rb')
        response = FileResponse(zip_file, content_type='application/orce-download')
        response['Content-Disposition'] = 'attachment; filename=name.zip'
        return response