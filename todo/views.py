from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_list_or_404

from .models import Task

# Create your views here.
def index(request: HttpRequest):
    todo_list = get_list_or_404(Task)
    return render(request, 'todo/index.html', context={'todo_list': todo_list})

def add_todo(request: HttpRequest):
    if request.method == 'POST':
        # ! BUG: Max length for task string field isn't enforced.
        # ! Should check if string length <= 30 characters
        added_task = request.POST['new-task']
        Task.objects.create(task=added_task, completed=False)
    return HttpResponseRedirect('/')

def update_todo_list(request: HttpRequest):
    if request.method == 'POST':
        todo_list = Task.objects.all()
        for task in todo_list:
            if request.POST.get(f'task{task.pk}') == 'completed':
                task.completed = True
            else:
                task.completed = False
            task.save()
    return HttpResponseRedirect('/')
