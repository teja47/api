from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .serializer import PosterSerializer
from articles.models import Cast
class PosterListView(ListAPIView):
    queryset = Cast.objects.all()
    serializer_class=PosterSerializer

class PosterDetailView(RetrieveAPIView):
    queryset = Cast.objects.all()
    serializer_class=PosterSerializer
    lookup_field='name'
    lookup_url_kwarg="abc"
class PosterUpdateView(UpdateAPIView):
    queryset = Cast.objects.all()
    serializer_class=PosterSerializer
class PosterDestroyView(DestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class=PosterSerializer
