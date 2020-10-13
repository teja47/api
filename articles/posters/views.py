from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializer import PosterSerializer
from articles.models import Poster
class PosterListView(ListAPIView):
    queryset = Poster.objects.all()
    serializer_class=PosterSerializer

class PosterDetailView(RetrieveAPIView):
    queryset = Poster.objects.all()
    serializer_class=PosterSerializer
