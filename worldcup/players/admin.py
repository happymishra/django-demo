from django.contrib import admin

# Register your models here.

# import all the models from current directory(.) models.py file
from .models import *

admin.site.register(Team)
admin.site.register(PlayerInfo)
