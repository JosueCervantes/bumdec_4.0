from django.urls import path
from . import views #. es la ruta actual


urlpatterns = [
    #path('login/', views.login, name="Login"),
    path('tienda/', views.Shop, name="Shop"),
    path('registrar/', views.UsuarioCreate, name="Registrar"),
    path('book-list', views.bookList, name='book-list'),
    path('book-create', views.bookCreate, name='book-create'),
    path('book-update/<int:id>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:id>', views.bookDelete, name='book-delete'),
]
