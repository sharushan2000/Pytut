from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial , name='tutorial'),
    path('variable/', views.tutorial , name='variable'),
    path('datatype/', views.tutorial , name='data_type'),
    path('loops/', views.tutorial , name='loops'),
    path('condition/', views.tutorial , name='condition'),



]