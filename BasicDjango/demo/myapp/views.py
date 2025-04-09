from django.shortcuts import render, HttpResponse
from .models import TodoItem #ORM
# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all  #ORM
    return render(request, "todos.html", {"todos":items})