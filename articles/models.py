from django.db import models
from django.db.models.fields import DateField
from datetime import date

class Movie(models.Model):
    title=models.CharField(max_length=120,blank=False,null=False)
    content=models.TextField(null=False,blank=False)
    image=models.ImageField(null=False,blank=False)
    youtubeLink=models.TextField(blank=True)
    contentHead=models.TextField(blank=True)
    releaseDate=models.DateField(blank=True,default=date.today)
    cast=models.TextField(blank=True)
    def __str__(self):
        return self.title
class Trailer(models.Model):
    title=models.CharField(max_length=120)
    poster=models.ImageField(blank=True)
    short=models.TextField()
    def __str__(self):
        return self.title
class Poster(models.Model):
    id = models.BigIntegerField(primary_key = True)
    title=models.CharField(max_length=120)
    poster=models.ImageField()
    def __str__(self):
        return self.title

class Cast(models.Model):
    name=models.CharField(max_length=120)
    photos=models.ImageField(blank=True)
    avatar=models.ImageField(blank=True)
    awards=models.TextField(blank=True)
    content=models.TextField(blank=True)
    movies=models.TextField(blank=True)
    socialMedia=models.TextField(blank=True)
    DOB=models.DateField(blank=True,default=date.today)
    field=models.TextField(blank=True)
    def __str__(self):
        return self.name

class ArticalImage(models.Model):
    title=models.CharField(max_length=120)
    image=models.ImageField(blank=True)
    def __str__(self):
        return self.title

class webSeries(models.Model):
    title=models.CharField(max_length=120)
    image=models.ImageField()
    director=models.CharField(max_length=120)
    cast=models.TextField()
    trivia=models.TextField()
    storyLine=models.TextField()
    platform=models.CharField(max_length=120)
    category=models.TextField(max_length=120)
    releaseDate=models.DateField(blank=True)
    def __str__(self):
        return self.title