from rest_framework_json_api import serializers
from rest_framework_json_api.relations import *

from django.core.validators import *
from django.core.exceptions import ValidationError

from django.contrib.auth.models import *
from models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')

	def validateEmail(email):
		try:
			validate_email(email)
			return True
		except ValidationError:
			return False

class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	class Meta:
		model = Profile
		fields = ('id', 'user', 'wazeName', 'wazeLevel')

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('isVerified', 'venueId', 'name', 'permalink', 'lockLevel',
			'categories', 'number', 'street', 'city', 'state', 'country', 'createdBy',
			'createdOn', 'updatedBy', 'updatedOn', 'updateRequest', 'isResidential')
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
