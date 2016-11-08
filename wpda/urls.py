"""wpda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views
from api.views import *

router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("places", PlaceViewSet)

urlpatterns = [
	url(r'^api-auth-token/', obtain_auth_token),
	url(r'^admin/', admin.site.urls),

	# API
	url(r'^api/', include(router.urls)),
	#url(r'^places/?id=<venue_id>[^/]+)?', views.places, name='places'),

	# Frontend Ember app
	url(r'^', views.frontend, name='frontend')
]
