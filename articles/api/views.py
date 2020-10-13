from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializer import ArticalSerializer
from articles.models import Movie
class ArticalListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer

class ArticalDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer
