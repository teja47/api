from rest_framework import serializers
from articles.models import Poster

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Poster
        fields = ('id','title','poster')
