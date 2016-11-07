from api.models import *
from api.serializers import *

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render

class ProfileViewSet(viewsets.ModelViewSet):
	# Allows Profiles to accept CRUD operations
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
'''
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
'''
class PlaceViewSet(viewsets.ModelViewSet):
	# Allows Places to accept CRUD operations
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

def frontend(request):
	# Send requests for / to the Ember app
	return render(request, 'index.html', {})
