from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.addtask, name='addtask'),
    path('update/<int:id>', views.update_task, name='update'),
    path('delete/<int:id>', views.delete_task, name='delete'),
]