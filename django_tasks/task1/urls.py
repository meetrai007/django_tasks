from django.urls import path
from . import views

urlpatterns = [
 path('view-card', views.view_card, name='view_card'),   
]