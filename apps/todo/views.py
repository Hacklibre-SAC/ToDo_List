from django.shortcuts import render, redirect
from apps.todo.models import Todo
from apps.todo.forms import TodoForm
from django.contrib import messages


def todoList(request):
    form = TodoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            todo_name = request.POST.get("TodoName", "")
            messages.success(request, f"Se guardó la tarea {todo_name} SATISFACTORIAMENTE")
            return redirect("todolist")

    todo_lista = Todo.objects.all().order_by("-id")
    context = {"todo_list": todo_lista, "form": form }
    return render(request, "todo_list.html", context)

def update_todo_list(request, ide, state):
    todo = Todo.objects.filter(id=ide)
    todo_name = todo[0].TodoName
    todo.update(Status=state)

    if state:
        messages.success(request, f"Se cerró la tarea {todo_name} SATISFACTORIAMENTE.")
    else:
        messages.success(request, f"Se abrió la tarea {todo_name} SATISFACTORIAMENTE.")

    return redirect('todolist')


def delete_todo_list(request, ide):
    todo = Todo.objects.filter(id=ide)
    todo_name = todo[0].TodoName
    todo.delete()
    messages.success(request, f"Se eliminó la tarea {todo_name} SATISFACTORIAMENTE.")
    return redirect('todolist')