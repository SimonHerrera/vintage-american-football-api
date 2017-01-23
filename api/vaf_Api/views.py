from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from vaf_Api.models import Franchise, Manager, Equipment, Player, Location, Team, Game
from vaf_Api.serializers import FranchiseSerializer, ManagerSerializer, EquipmentSerializer, PlayerSerializer, LocationSerializer, TeamSerializer, GameSerializer


# Create your views here.
class FranchiseList(viewsets.ModelViewSet):
  queryset =Franchise.objects.all()
  serializer_class = FranchiseSerializer

class ManagerList(viewsets.ModelViewSet):
  queryset =Manager.objects.all()
  serializer_class = ManagerSerializer

class EquipmentList(viewsets.ModelViewSet):
  queryset =Equipment.objects.all()
  serializer_class = EquipmentSerializer

class PlayerList(viewsets.ModelViewSet):
  queryset =Player.objects.all()
  serializer_class = PlayerSerializer

class LocationList(viewsets.ModelViewSet):
  queryset =Location.objects.all()
  serializer_class = LocationSerializer

class TeamList(viewsets.ModelViewSet):
  queryset =Team.objects.all()
  serializer_class = TeamSerializer

class GameList(viewsets.ModelViewSet):
  queryset =Game.objects.all()
  serializer_class = GameSerializer