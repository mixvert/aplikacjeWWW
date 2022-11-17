from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
]