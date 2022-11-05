from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='hjome'),
  path('about/', views.about, name='about'),
  path('animals/', views.animals_index, name='animals_index')
]