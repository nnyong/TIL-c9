from django.db import models
from accounts.models import User

# Create your models here.Create
class Genre(models.Model):
    name=models.TextField()
    
class Movie(models.Model):
    title=models.TextField()
    audience=models.IntegerField()
    poster_url=models.TextField()
    description=models.TextField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    
class Score(models.Model):
    content=models.TextField()
    score=models.IntegerField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)