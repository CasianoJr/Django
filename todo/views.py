from django.shortcuts import render, redirect
from .models import Todo


def todo_view(request):
    context = {
        'todo_list': Todo.objects.all()
    }
    return render(request, 'todo.html', context)


def todo_add(request):
    if request.method == 'POST':
        item = Todo(name=request.POST['name'])
        if request.POST['name'] == '':
            return redirect('todo_view')
        item.save()
    return redirect('todo_view')


def todo_delete(request, pk):
    if request.method == 'POST':
        item = Todo.objects.get(pk=pk)
        item.delete()
    return redirect('todo_view')


def todo_mark_completed(request, pk):
    item = Todo.objects.get(pk=pk)
    item.completed = True
    item.save()
    return redirect('todo_view')


def todo_mark_incomplete(request, pk):
    item = Todo.objects.get(pk=pk)
    item.completed = False
    item.save()
    return redirect('todo_view')


def todo_delete_completed(request):
    if request.method == 'POST':
        Todo.objects.filter(completed__exact=True).delete()
    return redirect('todo_view')


def todo_delete_all(request):
    if request.method == 'POST':
        Todo.objects.all().delete()
    return redirect('todo_view')
