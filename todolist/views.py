from django.shortcuts import render,redirect

from .models import Todolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST
def index(request):
    todo_items = Todolist.objects.order_by('id')
    form=TodoListForm()

    context = {'todo_items' : todo_items, 'form' : form }
    return render(request,'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    print("hbsjf")
    if form.is_valid():
        print("yes")
        new_todo =Todolist(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completedTodo(request,todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed =True).delete()

    return redirect('index')




def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')
