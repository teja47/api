from django.urls import path
from .views import PosterDetailView,PosterListView

urlpatterns =[
    path('',PosterListView.as_view()),
    path('<abc>',PosterDetailView.as_view()),
   

]