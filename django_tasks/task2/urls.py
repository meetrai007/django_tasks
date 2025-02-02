from django.urls import path
from . import views

urlpatterns = [
    path('view-student', views.view_student, name='view_student'),
    path('add-student', views.add_student, name='add_student'),
]