from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from .models import Project, Task
from django.shortcuts import render, redirect
#from .forms import CreateNewTask, CreateNewProject
# Create your views here.
# Archivos HTML, CSS vistas

def index(request):
    return render(request, 'index.html')