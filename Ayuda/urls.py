from django.urls import path
from . import views #. es la ruta actual


urlpatterns = [
    path('', views.help, name="Ayuda")
]