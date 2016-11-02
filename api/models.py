from __future__ import unicode_literals
from django.db import models

class Profile(models.Model):
	#user_id = models.ForeignKey(User)
	waze_id = models.CharField(max_length=63, unique=True)

	def __str__(self):
		return self.user.username

class Place(models.Model):
	is_verified = models.BooleanField(default=False)
	venue_id = models.CharField(max_length=63, primary_key=True, editable=False)
	name = models.CharField(max_length=255)
	permalink = models.URLField(max_length=255, editable=False, unique=True)
	lock_level = models.PositiveSmallIntegerField(default=0)
	categories = models.CharField(max_length=255)
	number = models.CharField(max_length=63, blank=True)
	street = models.CharField(max_length=63, blank=True)
	city = models.CharField(max_length=63, blank=True)
	state = models.CharField(max_length=63)
	country = models.CharField(max_length=63)
	updated_by = models.CharField(max_length=63, blank=True)
	updated_on = models.DateTimeField(blank=True, null=True)
	user_report_on = models.DateTimeField(blank=True, null=True)
	is_residential = models.BooleanField(default=False)

	def __str__(self):
		return ' '.join([self.venue_id, self.name])
