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

  def __str__(self):
    return self.nameTeams

class Player(models.Model):
  firstName = models.CharField(max_length=20)
  lastName = models.CharField(max_length=25)
  jerseyNumber = models.IntegerField(max_length=2)

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