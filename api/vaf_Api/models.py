from django.db import models
from django.utils import timezone


year = [(number, number) for number in range(2015, 2020)]

# Create your models is next Step
class Game(models.Model):
  gameTitle = models.CharField(max_length=100)
  city = models.CharField(max_length=40)
  state = models.CharField(max_length=2)
  venueName = models.CharField(max_length=60)
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
  visitorScore = models.IntegerField(default=0)
  homeScore = models.IntegerField(default=0)
  visitor1st = models.IntegerField(default=0)
  visitor2nd = models.IntegerField(default=0)
  visitor3rd = models.IntegerField(default=0)
  visitor4th = models.IntegerField(default=0)
  home1st = models.IntegerField(default=0)
  home2nd = models.IntegerField(default=0)
  home3rd = models.IntegerField(default=0)
  home4th = models.IntegerField(default=0)
  image1 = models.ImageField(upload_to = 'game_images/', default = 'game_images/default_game_image.jpg')
  image2 = models.ImageField(upload_to = 'game_images/', blank=True)
  image3 = models.ImageField(upload_to = 'game_images/', blank=True)
  image4 = models.ImageField(upload_to = 'game_images/', blank=True)

  def __str__(self):
    return self.gameTitle

class Player(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=25)
  jerseyNumber = models.IntegerField()
  email = models.CharField(default="", max_length=40)
  phone = models.CharField(default="", max_length=14)
  image1 = models.ImageField(upload_to = 'player_images/', default = 'player_images/default_player_image.jpg')
  # image2 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image3 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image4 = models.ImageField(upload_to = 'player_images/', blank=True)

  def __str__(self):
    return '{0} {1}'.format(self.firstName, self.lastName)

class Team(models.Model):
  managerFirstName = models.CharField(max_length=20)
  managerLastName = models.CharField(max_length=25)
  primaryColor = models.CharField(max_length=25)
  secondaryColor = models.CharField(max_length=25)
  year = models.IntegerField(choices=year, default=2015)
  playerId = models.ForeignKey(Player, related_name='players', on_delete=models.SET_NULL, null=True)
  image = models.ImageField(upload_to = 'team_images/', default = 'team_images/default_team_image.jpg')

  # def __str__(self):
  #   return '{0} {1} - {2}'.format(self.cityName, self.teamName, year)

class Equipment(models.Model):
  ballType = models.CharField(max_length=10)
  ballMfg = models.CharField(max_length=30)

  # def __str__(self):
  #   return self.nameTeams

# going to add ball class with description, price stuff for sale and for use purposes
