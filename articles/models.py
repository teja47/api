from django.db import models

class Movie(models.Model):
    id = models.BigIntegerField(primary_key = True)
    title=models.CharField(max_length=120,blank=False,null=False)
    content=models.TextField(null=False,blank=False)
    image=models.ImageField(null=False,blank=False)
    youtubeLink=models.TextField(blank=True)
    contentHead=models.TextField(blank=True)
    cast=models.TextField(blank=True,default="000")
    def __str__(self):
        return self.title
class Trailer(models.Model):
    id = models.BigIntegerField(primary_key = True)
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
    id = models.BigIntegerField(primary_key = True)
    name=models.CharField(max_length=120)
    photos=models.ImageField(blank=True)
    avatar=models.ImageField(blank=True)
    awards=models.TextField(blank=True)
    content=models.TextField(blank=True)
    movies=models.TextField(blank=True)
    socialMedia=models.TextField(blank=True)
    age=models.IntegerField(blank=True)
    field=models.TextField(blank=True)
    def __str__(self):
        return self.name

