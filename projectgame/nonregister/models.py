from django.db import models
from distutils.text_file import TextFile
from numbers import Integral
from django.contrib.auth.models import User


# Create your models here.
class Regis(models.Model):
    fname = models.CharField(max_length=250, default="", editable=True)
    lname = models.CharField(max_length=250, default="", editable=True)
    username = models.CharField(max_length=50, default="", editable=True)
    password = models.CharField(max_length=50, default="", editable=True)
    email = models.CharField(max_length=50, default="", editable=True)


class Game_type(models.Model):
    type_name = models.CharField(max_length=255, default="", editable=True)
    
    def __str__(self):
        return self.type_name
    


    
class Game(models.Model):
    
    name = models.CharField(max_length=255, default="", editable=True)
    description = models.CharField(max_length=255, default="", editable=True)
    game_type_id = models.ForeignKey(Game_type, on_delete=models.PROTECT)
    developer = models.CharField(max_length=255, default="", editable=True)
    rating = models.CharField(max_length=255, default="", editable=True)
    release_date = models.DateTimeField()
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Image(models.Model):
    
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    img_url = models.ImageField(upload_to='static/static_dirs/images/')
    def __str__(self):
        return self.game_id.name

    
    

class User_Game(models.Model):
   
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_date = models.DateField(auto_now=True)
    serial = models.CharField(max_length=255, default="", editable=True)
