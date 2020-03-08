from django.contrib import admin
from nonregister.models import Regis, Game, Game_type, Image, User_Game
from django.contrib.auth.models import Permission




admin.site.register(Permission)
admin.site.register(Regis)
admin.site.register(Game)
admin.site.register(Game_type)
admin.site.register(Image)
admin.site.register(User_Game)

# Register your models here.
