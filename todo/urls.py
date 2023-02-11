from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add-todo', views.add_todo, name='add todo'),
    path('update-todo-list', views.update_todo_list, name='update todo list')
]
