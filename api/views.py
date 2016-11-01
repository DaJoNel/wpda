#from django.db import models
#from django.contrib.auth.models import *

from api.models import *
from api.serializers import *

from rest_framework import viewsets
#from rest_framework.views import APIView
#from rest_framework.response import Response

#from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from django.shortcuts import render
'''
class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
'''
class PlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

def home(request):
	# Send requests for / to the Ember app
	return render(request, 'index.html', {},)
