from rest_framework import serializers
from articles.models import ArticalImage

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model =ArticalImage
        fields = ('id','title','image')
