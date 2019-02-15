from django.shortcuts import render,redirect

from .models import Todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST
def index(request):
    todo_items = Todolist.objects.order_by('id')
    form=TodoListForm()

    context = {'todo_items' : todo_items, 'form' : form }
    return render(request,' todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = todoListForm(request.POST)

    print(request.POST['text'])
    return redirect('index')

