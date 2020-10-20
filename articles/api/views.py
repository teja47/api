from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .serializer import ArticalSerializer
from articles.models import Movie
class ArticalListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer

class ArticalDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer
class ArticalUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer
class ArticalDestroyView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer
class ArticalcreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class=ArticalSerializer