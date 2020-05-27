from django.shortcuts import render, redirect
from .models import AddTask
from .forms import SubmitNewTask


def home(request):
    todo = AddTask.objects.all()
    form = SubmitNewTask()

    if request.method == 'POST':
        form = SubmitNewTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        context = {'todo': todo, 'form': form}
        return render(request, 'todo/home.html', context)


def updatetask(request, pk):
    # task_to_update = AddTask.objects.get(pk=pk)
    return render(request, 'todo/update_task.html')
