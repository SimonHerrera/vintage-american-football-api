from vaf_Api.models import Franchise, Manager, Equipment, Player, Location, Team, Game
from rest_framework import serializers
# from rest_framework.serializers import (ModelSerializer, HyperlinkedIdentityField, SerializerMethodField)
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt #RT csrf crashed until I added

class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Franchise
    fields = ('id', 'url', 'vafEstablished', 'aboutOrgTeamParagraph', 'aboutOrgTeamParagraph2')

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Equipment
    fields = ('id', 'url', 'ballType', 'ballMfg')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Player
    fields = ('id', 'url', 'firstName', 'lastName', 'email', 'phone', 'image1')
    # fields = ('id', 'url', 'firstName', 'lastName', 'jerseyNumber', 'image1', 'image2', 'image3', 'image4')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
      model = Location
      fields = ('id', 'url', 'city', 'state', 'venueName')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
  # teams = TeamSerializer(many=True)
  class Meta:
    model = Manager
    fields = ('id', 'url', 'firstName', 'lastName', 'email', 'phone')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
  managerId = ManagerSerializer() # turn off to add managers - turn on to allow it to be seen in angular
  # playerId = PlayerSerializer()
  # managerId = SerializerMethodField()
  class Meta:
    model = Team
    fields = ('id', 'url', 'cityName', 'teamName', 'primaryColor', 'secondaryColor', 'year', 'managerId', 'playerId', 'image', 'imageInfo')

  # def get_managerId(self, obj)
  #   return str(obj.managerId.firstName)


class GameSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'url', 'location', 'date', 'visitorTeam', 'homeTeam', 'visitorScore', 'homeScore', 'visitor1st', 'visitor2nd', 'visitor3rd', 'visitor4th', 'home1st', 'home2nd', 'home3rd', 'home4th', 'ball', 'image1', 'image2', 'image3', 'image4')

# #Need for superuser Auth
# @csrf_exempt
# def login_user(request):
#     '''Handles the creation of a new user for authentication

#     Method arguments:
#       request -- The full HTTP request object
#     '''

#     # Load the JSON string of the request body into a dict
#     req_body = json.loads(request.body.decode())

#     # Use the built-in authenticate method to verify
#     authenticated_user = authenticate(
#             username=req_body['username'],
#             password=req_body['password']
#             )

#     # If authentication was successful, log the user in
#     success = True
#     if authenticated_user is not None:
#         login(request=request, user=authenticated_user)
#     else:
#         success = False

#     data = json.dumps({"success":success})
#     return HttpResponse(data, content_type='application/json')