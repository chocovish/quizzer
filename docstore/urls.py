from django.urls import path
from docstore import views
urlpatterns = [
    path('', views.home, name="home"),
    path('play/', views.play, name='play'),
    path('completed/', views.completed,name="completed"),
    path('add/', views.add, name='add'),
]
