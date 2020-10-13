from rest_framework import serializers
from articles.models import Cast

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cast
        fields = ('id','name','avatar','age','photos','content','awards','socialMedia','movies')
