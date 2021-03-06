from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
from django.contrib.auth.models import *
from django.contrib import admin

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	wazeName = models.CharField(max_length=255)
	wazeLevel = models.PositiveSmallIntegerField(default=1)

	def __str__(self):
		return self.user.username

	class Admin(admin.ModelAdmin):
		list_display = ('user',)

	class JSONAPIMeta:
		resource_name = "profiles"

class Place(models.Model):
	isVerified = models.BooleanField(default=False)
	venueId = models.CharField(max_length=63, primary_key=True, editable=False)
	name = models.CharField(max_length=255)
	permalink = models.URLField(max_length=255, editable=False, unique=True)
	lockLevel = models.PositiveSmallIntegerField(default=0)
	categories = models.CharField(max_length=255)
	number = models.CharField(max_length=63, null=True)
	street = models.CharField(max_length=63, null=True)
	city = models.CharField(max_length=63, null=True)
	state = models.CharField(max_length=63)
	country = models.CharField(max_length=63)
	createdBy = models.CharField(max_length=63, null=True)
	createdOn = models.DateTimeField(null=True)
	updatedBy = models.CharField(max_length=63, null=True)
	updatedOn = models.DateTimeField(null=True)
	updateRequest = models.BooleanField(default=False)
	isResidential = models.BooleanField(default=False)

	def __str__(self):
		return ' '.join([self.venue_id, self.name])

	class JSONAPIMeta:
		resource_name = "places"
