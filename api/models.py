from __future__ import unicode_literals
from django.db import models

class Profile(models.Model):
	#user_id = models.ForeignKey(User)
	wazeId = models.CharField(max_length=63, unique=True)

	def __str__(self):
		return self.user.username

class Place(models.Model):
	isVerified = models.BooleanField(default=False)
	venueId = models.CharField(max_length=63, primary_key=True, editable=False)
	name = models.CharField(max_length=255)
	permalink = models.URLField(max_length=255, editable=False, unique=True)
	lockLevel = models.PositiveSmallIntegerField(default=0)
	categories = models.CharField(max_length=255)
	number = models.CharField(max_length=63, blank=True)
	street = models.CharField(max_length=63, blank=True)
	city = models.CharField(max_length=63, blank=True)
	state = models.CharField(max_length=63)
	country = models.CharField(max_length=63)
	createdBy = models.CharField(max_length=63, blank=True)
	createdOn = models.DateTimeField(blank=True, null=True)
	updatedBy = models.CharField(max_length=63, blank=True)
	updatedOn = models.DateTimeField(blank=True, null=True)
	updateRequest = models.BooleanField(default=False)
	isResidential = models.BooleanField(default=False)

	def __str__(self):
		return ' '.join([self.venue_id, self.name])
