from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from vaf_Api.models import Game, Player, Team, Equipment
from vaf_Api.serializers import GameSerializer, PlayerSerializer, TeamSerializer, EquipmentSerializer

# Create your views here.
class GameList(viewsets.ModelViewSet):
  queryset =Game.objects.all()
  serializer_class = GameSerializer

class PlayerList(viewsets.ModelViewSet):
  queryset =Player.objects.all()
  serializer_class = PlayerSerializer

class TeamList(viewsets.ModelViewSet):
  queryset =Team.objects.all()
  serializer_class = TeamSerializer

class EquipmentList(viewsets.ModelViewSet):
  queryset =Equipment.objects.all()
  serializer_class = EquipmentSerializer