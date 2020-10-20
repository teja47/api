from django.urls import path
from .views import PosterDetailView,PosterListView,PosterDestroyView,PosterUpdateView,PostercreateView

urlpatterns =[
    path('',PosterListView.as_view()),
    path('<pk>',PosterDetailView.as_view()),
    path('<pk>/delete',PosterDestroyView.as_view()),
    path('update',PosterUpdateView.as_view()),
    path('create/pos/',PostercreateView.as_view())
   

]