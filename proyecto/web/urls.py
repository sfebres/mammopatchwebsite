from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('about/', views.about, name='about'),
]