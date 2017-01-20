from django.db import models
from django.utils import timezone


year = [(number, number) for number in range(2015, 2020)]

# Create your models is next Step
class Manager(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=25)
  email = models.CharField(default="", max_length=40)
  phone = models.CharField(default="", max_length=14)

  def __str__(self):
    # return self.lastName #only showed part of name, now shows all, is that legit?
    return '{0} {1}'.format(self.firstName, self.lastName)

class Equipment(models.Model):
  # ballType = models.CharField(max_length=10)
  ballType = models.CharField(default="", max_length=45)
  ballMfg = models.CharField(default="", max_length=45)
  # ballMfg = models.CharField(max_length=30)

  def __str__(self):
    return '{0} - {1}'.format(self.ballType, self.ballMfg)

class Player(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=25)
  email = models.CharField(default="", max_length=40)
  phone = models.CharField(default="", max_length=14)
  image1 = models.ImageField(upload_to = 'player_images/', default = 'player_images/default_player_image.jpg')
  # image2 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image3 = models.ImageField(upload_to = 'player_images/', blank=True)
  # image4 = models.ImageField(upload_to = 'player_images/', blank=True)

  def __str__(self):
    return '{0} {1}'.format(self.firstName, self.lastName)

class Location(models.Model):
  city = models.CharField(default='', max_length=40)
  state = models.CharField(default='', max_length=2)
  venueName = models.CharField(default='', max_length=50)

  def __str__(self):
    return '{0} {1} - {2}'.format(self.city, self.state, self.venueName)

class Team(models.Model):
  cityName = models.CharField(default="", max_length=45)
  teamName = models.CharField(default="", max_length=45)
  primaryColor = models.CharField(max_length=25)
  secondaryColor = models.CharField(max_length=25)
  year = models.IntegerField(choices=year, default=2015)
  managerId = models.ForeignKey(Manager, related_name='teams', on_delete=models.SET_NULL, null=True)
  playerId = models.ManyToManyField(Player)
  # want many to many here because its natural that a team has many players and rare a player plays on many teams
  # playerId = models.ForeignKey(Player, related_name='players', on_delete=models.SET_NULL, null=True)
  image = models.ImageField(upload_to = 'team_images/', default = 'team_images/default_team_image.jpg')

  def __str__(self):
    return '{0} {1} - {2}'.format(self.cityName, self.teamName, self.year)

class Game(models.Model):
  location = models.ForeignKey(Location, related_name='games', on_delete=models.SET_NULL, null=True)
  date = models.DateField(auto_now=False, auto_now_add=False)
  visitorTeam = models.ForeignKey(Team, related_name='visitoTeam', on_delete=models.SET_NULL, null=True)
  homeTeam = models.ForeignKey(Team, related_name='homeTeam', on_delete=models.SET_NULL, null=True)
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
  ball = models.ForeignKey(Equipment, related_name='games', on_delete=models.SET_NULL, null=True)
  image1 = models.ImageField(upload_to = 'game_images/', default = 'game_images/default_game_image.jpg')
  image2 = models.ImageField(upload_to = 'game_images/', blank=True)
  image3 = models.ImageField(upload_to = 'game_images/', blank=True)
  image4 = models.ImageField(upload_to = 'game_images/', blank=True)

  # def __str__(self):
  #   return self.gameTitle


# going to add ball class with description, price stuff for sale and for use purposes
