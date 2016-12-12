from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

# REST API
from rest_framework import viewsets, filters
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

# Import filters
from api.serializers import *
from api.pagination import *

class Register(APIView):
	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		wazeName = request.POST.get('wazeName')
		wazeLevel = request.POST.get('wazeLevel')

		print request.POST.get('username')
		if User.objects.filter(username=username).exists():
			return Response({'username': 'Username is taken.', 'status': 'error'})
		elif User.objects.filter(email=email).exists():
			return Response({'email': 'Email is taken.', 'status': 'error'})

		newuser = User.objects.create_user(email=email, username=username, password=password)
		newprofile = Profile(user=newuser, wazeName=wazeName, wazeLevel=wazeLevel)
		newprofile.save()

		return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})

class Session(APIView):
	permission_classes = (AllowAny,)
	def form_response(self, isauthenticated, userid, username, error=""):
		data = {
			'isauthenticated': isauthenticated,
			'userid': userid,
			'username': username
		}
		if error:
			data['message'] = error

		return Response(data)

	def get(self, request, *args, **kwargs):
		# Get the current user
		if request.user.is_authenticated():
			return self.form_response(True, request.user.id, request.user.username)
		return self.form_response(False, None, None)

	def post(self, request, *args, **kwargs):
		# Login
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return self.form_response(True, user.id, user.username)
			return self.form_response(False, None, None, "Account is suspended")
		return self.form_response(False, None, None, "Invalid username or password")

	def delete(self, request, *args, **kwargs):
		# Logout
		logout(request)
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
	resource_name = 'users'
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
	resource_name = 'profiles'
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class PlaceViewSet(viewsets.ModelViewSet):
	resource_name = 'places'
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

def frontend(request):
	# Send requests for / to the Ember app
	return render(request, 'index.html', {})
