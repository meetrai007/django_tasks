from django.urls import path
from . import views

urlpatterns = [
    path('get-todos', views.get_todos, name='get_todos'),
    path('create-todo', views.create_todo, name='create_todo'),
    path('update-todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete_todo'),
]