from django.urls import path
from .views import ArticalDetailView,ArticalListView,ArticalDestroyView,ArticalUpdateView,ArticalcreateView

urlpatterns =[
    path('',ArticalListView.as_view()),
    path('<pk>',ArticalDetailView.as_view()),
    path('create/api/',ArticalcreateView.as_view()),
    path('<pk>/delete',ArticalDestroyView.as_view()),
    path('update/api/',ArticalUpdateView.as_view())
    

]