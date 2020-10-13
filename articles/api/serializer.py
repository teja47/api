from rest_framework import serializers
from articles.models import Movie

class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model =Movie
        fields = ('id','title','content','image','youtubeLink','contentHead','cast')
