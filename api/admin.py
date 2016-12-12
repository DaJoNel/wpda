from django.contrib import admin
from models import *

admin.site.register(Profile, Profile.Admin)
admin.site.register(Place)
