from rest_framework import serializers
from articles.models import Cast

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cast
        fields = ('name','avatar','DOB','photos','content','awards','socialMedia','movies')
