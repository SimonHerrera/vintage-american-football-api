from vaf_Api.models import Game, Player, Team, Equipment
from rest_framework import serializers



class GameSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'url', 'gameTitle', 'city', 'state', 'venueName', 'season', 'date')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Player
    fields = ('id', 'url', 'firstName', 'lastName', 'jerseyNumber')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Team
    fields = ('id', 'url', 'name', 'managerFirstName', 'managerLastName', 'primaryColor', 'secondaryColor')

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Equipment
    fields = ('id', 'url', 'ballType', 'ballMfg')

