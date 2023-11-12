from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('sosmed', views.sosmed, name='sosmed'),
  

]