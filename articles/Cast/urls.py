from django.urls import path
from .views import PosterDetailView,PosterListView,PosterDestroyView,PosterUpdateView

urlpatterns =[
    path('',PosterListView.as_view()),
    path('<abc>',PosterDetailView.as_view()),
    path('<abc>/delete',PosterDestroyView.as_view()),
    path('update',PosterUpdateView.as_view())
   

]