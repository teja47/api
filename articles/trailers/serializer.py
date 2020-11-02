from rest_framework import serializers
from articles.models import Trailer

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model =Trailer
        fields = ('title','short','poster')
