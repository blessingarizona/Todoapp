from django.shortcuts import render, redirect
from .models import mytodo
from .forms import TodoForm

# Create your views here.
def index(request):
    tasks = mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

def deleteItem(request, pk):
    task = mytodo.objects.get(id = pk)
    task.delete()
    return redirect('index')

def updateItem(request, pk):
    todo = mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance=todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('index')
    return render(request, 'updateItem.html', {'todo':todo, 'updateForm': updateForm})