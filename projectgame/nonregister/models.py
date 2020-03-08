from django.db import models

# Create your models here.
class Regis(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Game_type(models.Model):
    
    type_name = models.CharField(max_length=255, default="", editable=False)
    
class Game(models.Model):
    
    name = models.CharField(max_length=255, default="", editable=False)
    description = models.CharField(max_length=255, default="", editable=False)
    game_type_id = models.ForeignKey(Game_type, on_delete=models.PROTECT)
    developer = models.CharField(max_length=255, default="", editable=False)
    rating = models.CharField(max_length=255, default="", editable=False)
    price = models.IntegerField()


class Image(models.Model):
    
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)
    img_url = models.ImageField(upload_to='')

class User_Game(models.Model):
   
    user_id = models.ForeignKey(Regis, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchased_date = models.DateTimeField()
    serial = models.CharField(max_length=255, default="", editable=False)