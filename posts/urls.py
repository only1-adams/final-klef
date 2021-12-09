from django.urls import path 
from . import views

urlpatterns = [
    path('postsss/', views.post, name='post')
]