from django.urls import path
from .views import ArticalDetailView,ArticalListView

urlpatterns =[
    path('',ArticalListView.as_view()),
    path('<pk>',ArticalDetailView.as_view()),
   

]