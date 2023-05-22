from django.contrib import admin
from django.urls import path
from apps.todo.views import todoList, update_todo_list, delete_todo_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoList, name='todolist'),
    path('update/<int:ide>/<int:state>', update_todo_list, name='update_todo_list'),
    path('delete/<int:ide>/', delete_todo_list, name='delete_todo_list')
]
