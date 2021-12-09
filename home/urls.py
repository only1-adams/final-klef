from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>/<slug:slug>', views.postdetails, name='postdetails'),
    path('about/', views.about, name='about'),
    path('results/', views.search, name='search'),
    path('allpost/<str:id>/<slug:slug>', views.catposti, name='catposti'),
    path('promotion/', views.promotion, name='promotion'),
    path('privacy/', views.privacy, name='privacy'),
]