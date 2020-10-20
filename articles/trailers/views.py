from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .serializer import PosterSerializer
from articles.models import Trailer
class PosterListView(ListAPIView):
    queryset = Trailer.objects.all()
    serializer_class=PosterSerializer

class PosterDetailView(RetrieveAPIView):
    queryset = Trailer.objects.all()
    serializer_class=PosterSerializer
class PosterUpdateView(UpdateAPIView):
    queryset = Trailer.objects.all()
    serializer_class=PosterSerializer
class PosterDestroyView(DestroyAPIView):
    queryset = Trailer.objects.all()
    serializer_class=PosterSerializer
class PosterCreateView(CreateAPIView):
    queryset = Trailer.objects.all()
    serializer_class=PosterSerializer
