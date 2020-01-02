from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todos
# Create your views here.
def index(request):
    all_todo_items = Todos.objects.all()
    return render(request, 'todos.html', {'all_items': all_todo_items})
def addTodo(request):
    new_item=Todos(content =request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todos/')
def deleteTodo(request, todo_id):
    delete_item=Todos.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todos/')
