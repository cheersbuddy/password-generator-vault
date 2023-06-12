from . import views 
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('home/char/', views.char, name='char'),
   
    
]