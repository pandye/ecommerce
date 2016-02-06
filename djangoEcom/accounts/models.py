from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class State(models.Model):
	name = models.CharField(max_length=20)
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=20)
	state = models.ForeignKey(State)

	def __str__(self):
		return self.name

class Address(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField()
    address1 = models.TextField()
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    city = models.ForeignKey(City)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
		return self.user.username
