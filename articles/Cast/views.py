from rest_framework.generics import ListAPIView,RetrieveAPIView
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