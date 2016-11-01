from rest_framework import serializers
from models import Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('venue_id', 'name', 'permalink', 'lock_level', 'categories', 
			'number', 'street', 'city', 'state', 'country', 'updated_by', 
			'updated_on', 'user_report_on', 'is_residential')
