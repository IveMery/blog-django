from django.urls import path
from .views import * 

urlpatterns = [
    path('home/',boardsView,name='home'),
    path('home/<int:pk>/', board_topicsView, name='board_topics'),
]