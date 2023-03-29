from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants, name='plants'),
    path('techniques/', views.techniques, name='techniques'),
    path('texnika/', views.texnika, name='texnika'),
    path('tools/', views.tools, name='tools'),
    path('watering/', views.watering, name='watering'),
    path('watering/<int:id>/', views.watering_item, name='watering_item'),
    path('fertilizers/', views.fertilizers, name='fertilizers'),
    path('fertilizers/<int:id>/', views.fertilizer_item, name='fertilizer_item'),
    path('news/', views.news, name='news'),
    path('texnika/<int:id>/', views.texnika_tool, name='texnika-tool'),
    path('plants/<int:id>/', views.plant_type, name='plant-type'),
    path('plants/type/<int:id>/', views.type, name='type'),
]
