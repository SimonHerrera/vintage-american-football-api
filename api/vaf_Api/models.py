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

class Franchise(models.Model):
  FranCityName = models.CharField(default="", max_length=45)
  FranTeamName = models.CharField(default="", max_length=45)
  vafEstablished = models.DateField(auto_now=False, auto_now_add=False)
  aboutVafTeam1 = models.TextField(default="", max_length=400)
  aboutVafTeam2 = models.TextField(default="", max_length=400)
  aboutOrgTeam1 = models.TextField(default="", max_length=400)
  aboutOrgTeam2 = models.TextField(default="", max_length=400)
  franchiseLogo = models.ImageField(upload_to = 'franchise_images/', default = 'franchise_images/default_franchise_image.jpg')

def __str__(self):
    return '{0} {1}'.format(self.FranCityName, self.FranTeamName)

class Equipment(models.Model):
  ballType = models.CharField(default="", max_length=45)
  ballMfg = models.CharField(default="", max_length=45)

  def __str__(self):
    return '{0} - {1}'.format(self.ballType, self.ballMfg)

class Player(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=25)
  email = models.CharField(default="", max_length=40)
  phone = models.CharField(default="", max_length=14)
  image1 = models.ImageField(upload_to = 'player_images/', default = 'player_images/default_player_image.jpg')
  image1Info = models.CharField(default="", max_length=100)
  playerInfo = models.TextField(default="", max_length=200)

  def __str__(self):
    return '{0} {1}'.format(self.firstName, self.lastName)

class Location(models.Model):
  city = models.CharField(default="", max_length=40)
  state = models.CharField(default="", max_length=2)
  venueName = models.CharField(default="", max_length=50)

  def __str__(self):
    return '{0} {1} - {2}'.format(self.city, self.state, self.venueName)

class Team(models.Model):
  franchiseId = models.ForeignKey(Franchise, related_name='franchiseId', on_delete=models.SET_NULL, null=True)
  managerId = models.ForeignKey(Manager, related_name='managerId', on_delete=models.SET_NULL, null=True)
  playerId = models.ManyToManyField(Player)
  cityName = models.CharField(default="", max_length=45)
  teamName = models.CharField(default="", max_length=45)
  year = models.IntegerField(choices=year, default=2015)
  primaryColor = models.CharField(max_length=25)
  secondaryColor = models.CharField(max_length=25)
  # want many to many here because its natural that a team has many players and rare a player plays on many teams
  image = models.ImageField(upload_to = 'team_images/', default = 'team_images/default_team_image.jpg')
  imageInfo = models.CharField(default="", max_length=100)

  def __str__(self):
    return '{0} {1} - {2}'.format(self.cityName, self.teamName, self.year)

class Game(models.Model):
  visitorTeam = models.ForeignKey(Team, related_name='visitorTeam', on_delete=models.SET_NULL, null=True)
  homeTeam = models.ForeignKey(Team, related_name='homeTeam', on_delete=models.SET_NULL, null=True)
  equipmentId = models.ForeignKey(Equipment, related_name='games', on_delete=models.SET_NULL, null=True)
  locationId = models.ForeignKey(Location, related_name='games', on_delete=models.SET_NULL, null=True)
  date = models.DateField(auto_now=False, auto_now_add=False)
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
  image1Info = models.CharField(default="", max_length=100)
  gameSummary = models.TextField(default="", max_length=400)
  gameSummary2 = models.TextField(default="", max_length=400)
  image2 = models.ImageField(upload_to = 'game_images/', blank=True)
  image3 = models.ImageField(upload_to = 'game_images/', blank=True)
  image4 = models.ImageField(upload_to = 'game_images/', blank=True)

  # def __str__(self):
  #   return self.gameTitle


# going to add ball class with description, price stuff for sale and for use purposes
