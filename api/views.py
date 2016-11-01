from rest_framework import viewsets
from models import Place
from serializers import PlaceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PlaceViewSet(viewsets.ModelViewSet):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
