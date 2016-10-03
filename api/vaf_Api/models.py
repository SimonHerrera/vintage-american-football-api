from django.db import models
from django.utils import timezone


season = [(number, number) for number in range(2015, 2020)]

# Create your models is next Step
class Game(models.Model):
  gameTitle = models.CharField(max_length=100)
  city = models.CharField(max_length=40)
  state = models.CharField(max_length=2)
  venueName = models.CharField(max_length=60)
  season = models.IntegerField(choices=season)
  date = models.DateTimeField(auto_now=False, auto_now_add=False)
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
  image1 = models.ImageField(upload_to = 'player_images/', default = 'player_images/default_player_image.jpg')
  # image2 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image3 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image4 = models.ImageField(upload_to = 'player_images/', blank=True)

  def __str__(self):
    return '{0} {1}'.format(self.firstName, self.lastName)

class Team(models.Model):
  name = models.CharField(max_length=40)
  managerFirstName = models.CharField(max_length=20)
  managerLastName = models.CharField(max_length=25)
  primaryColor = models.CharField(max_length=25)
  secondaryColor = models.CharField(max_length=25)

  def __str__(self):
    return self.name

class Equipment(models.Model):
  ballType = models.CharField(max_length=10)
  ballMfg = models.CharField(max_length=30)

  # def __str__(self):
  #   return self.nameTeams

# going to add ball class with description, price stuff for sale and for use purposes
