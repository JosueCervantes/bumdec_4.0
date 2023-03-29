from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
#from .models import Project, Task
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, UsuarioForm
#from .forms import CreateNewTask, CreateNewProject
from .models import Usuarios
import Tienda

# Create your views here.
# Archivos HTML, CSS vistas

#def login(request):
    #if request.method == "GET":
     #   print("enviando formulario")
    #else:
     #   print(request.POST)
      #  print("obteniendo datos")
    
    #return render(request, 'login.html')

#class HomeView(LoginRequiredMixin, TemplateView):
 #   template_name = "index.html"

def registrar(request):
    return render(request, 'regsiter.html')

#@login_required
#def home(request):
 #   return render(request, 'index.html')

# Vistas de libros.
def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('book-list')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/book-list')  
            except Exception as e: 
                pass    
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')

#Vistas Usuarios
def UsuarioCreate(request):  
    if request.method == "POST":  
        form = UsuarioForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tienda')  
            except:  
                pass  
    else:  
        form = UsuarioForm()  
    return render(request,'regsiter.html',{'form':form})  

def Shop(request):  
    return render(request,"shop.html") 

def UsuarioRead(request, usuario):
    Users = Usuarios.objects.get(usuario=usuario)  
    if usuario in Users:
        form = UsuarioForm(request.POST)  
        return render(request, "shop.html")
    else:
        return render(request,"login.html")
    