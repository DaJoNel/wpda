from rest_framework import serializers
from models import *
#from django.contrib.auth.models import *
'''
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'url')

class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Profile
		fields = ('id', 'user', 'waze_id')
		depth = 1
'''
class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('is_verified', 'venue_id', 'name', 'permalink', 'lock_level', 
			'categories', 'number', 'street', 'city', 'state', 'country', 
			'updated_by', 'updated_on', 'user_report_on', 'is_residential')
	'''
	def validate_name(self, value):
		if '' not in value.lower():
			raise serializers.ValidationError("WARN: Failed WMEPH validation")
		return value
	'''
	def validate_lock_level(self, value):
		if value < 3:
			raise serializers.ValidationError("WARN: Low lock level detected")
		return value

	def validate_number(self, value):
		if value == "":
			raise serializers.ValidationError("ERROR: Place must have a number")
		return value

	def validate_street(self, value):
		if value == "":
			raise serializers.ValidationError("ERROR: Place must have a street")
		return value

	def validate_city(self, value):
		if value == "":
			raise serializers.ValidationError("ERROR: Place must have a city")
		return value