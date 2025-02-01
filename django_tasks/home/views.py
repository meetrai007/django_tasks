from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Tasks

# Create your views here.
def index(request):
    tasks = Tasks.objects.all().order_by('task')
    return render(request, 'home/index.html', {'tasks': tasks})

def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'home/taskform.html', {'form': form})

def update_task(request, id):
    task = Tasks.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'home/taskform.html', {'form': form})

def delete_task(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'home/delete_task.html', {'task': task})