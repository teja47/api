from django.urls import path
from .views import PosterDetailView,PosterListView,PosterDestroyView,PosterUpdateView,PosterCreateView

urlpatterns =[
    path('',PosterListView.as_view()),
    path('<abc>',PosterDetailView.as_view()),
    path('<abc>/delete',PosterDestroyView.as_view()),
    path('update',PosterUpdateView.as_view()),
    path('create/cast/',PosterCreateView.as_view()),
   

]