from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:handle>/', views.profile, name='profile'),
]
