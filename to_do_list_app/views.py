from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UniqueTodoForm
from .models import UniqueTodo

def todo_list(request):
    if request.method == "POST":
        form = UniqueTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = UniqueTodoForm()
    todo_items = UniqueTodo.objects.filter(completed=False)
    completed_tasks = UniqueTodo.objects.filter(completed=True)
    context = {
        "form": form,
        "active_tasks": todo_items,
        "completed_tasks": completed_tasks,
        "title": "TODO LIST",
    }
    return render(request, 'base.html', context)

def mark_as_completed(request, item_id):
    item = get_object_or_404(UniqueTodo, pk=item_id)
    item.completed = True
    item.save()
    messages.info(request, "Task marked as completed!")
    return redirect('todo_list')

def remove_todo(request, item_id):
    item = get_object_or_404(UniqueTodo, pk=item_id)
    item.delete()
    messages.info(request, "Task deleted successfully!")
    return redirect('todo_list')
