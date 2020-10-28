from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from .serializer import PosterSerializer
from articles.models import ArticalImage
class PosterListView(ListAPIView):
    queryset = ArticalImage.objects.all()
    serializer_class=PosterSerializer

class PosterDetailView(RetrieveAPIView):
    queryset = ArticalImage.objects.all()
    serializer_class=PosterSerializer
class PosterUpdateView(UpdateAPIView):
    queryset = ArticalImage.objects.all()
    serializer_class=PosterSerializer
class PosterDestroyView(DestroyAPIView):
    queryset = ArticalImage.objects.all()
    serializer_class=PosterSerializer
class PosterCreateView(CreateAPIView):
    queryset = ArticalImage.objects.all()
    serializer_class=PosterSerializer
