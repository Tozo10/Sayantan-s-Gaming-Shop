from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.abouts, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
   
]
