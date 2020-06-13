from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import TaskForm, Task
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def tasks(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST or None)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            form = TaskForm()
        tasks = Task.objects.filter(user=request.user).order_by('priority')
        return render(request, 'tasks/tasks.html', {'form': form, 'tasks': tasks, 'user': request.user})

        # this is where GET request are accessed
    form = TaskForm()
    tasks = Task.objects.filter(user=request.user).order_by('priority')
    return render(request, 'tasks/tasks.html', {'form': form, 'tasks': tasks, 'user': request.user})


@login_required(login_url='/accounts/login/')
def delete(request, id):
    Task.objects.filter(id=id, user=request.user).delete()
    return redirect(reverse('tasks:all_task'))


@login_required(login_url='/accounts/login/')
def complete(request, id):
    task = Task.objects.filter(id=id, user=request.user)[0]
    if task.complete:
        task.complete = 0
    else:
        task.complete = 1
    task.save()
    return redirect('tasks:all_task')



@login_required(login_url='/accounts/login/')
def clear(request):
    tasks = Task.objects.filter(user=request.user)
    for task in tasks:
        task.delete()
    return redirect('tasks:all_task')
