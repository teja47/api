from rest_framework import serializers
from articles.models import webSeries


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = webSeries
        fields = ('title', 'trivia', 'image', 'director', 'cast',
                  'storyLine', 'platform', 'category', 'releaseDate')
