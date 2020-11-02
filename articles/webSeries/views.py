from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializer import ArticalSerializer
from articles.models import webSeries


class ArticalListView(ListAPIView):
    queryset = webSeries.objects.all()
    serializer_class = ArticalSerializer


class ArticalDetailView(RetrieveAPIView):
    queryset = webSeries.objects.all()
    serializer_class = ArticalSerializer
    lookup_field = 'title'
    lookup_url_kwarg = "abc"


class ArticalUpdateView(UpdateAPIView):
    queryset = webSeries.objects.all()
    serializer_class = ArticalSerializer


class ArticalDestroyView(DestroyAPIView):
    queryset = webSeries.objects.all()
    serializer_class = ArticalSerializer


class ArticalcreateView(CreateAPIView):
    queryset = webSeries.objects.all()
    serializer_class = ArticalSerializer
