from django.forms import ModelForm
from .models import Book, Usuarios

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'