"""BumDec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

#include incluye un bloque de urls
#puedo solamente mandar a llamar el archivo y todas sus vistas y especificar en las rutas la vista y funcion
from django.views.generic.base import TemplateView
#URLS que los usuarios puedan visitar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ayuda/', include('Ayuda.urls')), #a menos que tengamos muy divididos las rutas se '' vacio, se pone carpeta + archivo
    path('', include('Home.urls')),
    path('nosotros/', include('Nosotros.urls')),
    path('registrar/', include('Registrar.urls')),
    #path("cuentas/", include("cuentas.urls")),
    #path('login/', include('Registrar.urls')),
    path('tienda/', include('Tienda.urls')),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # Login and Logout
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("", TemplateView.as_view(template_name="shop.html"), name="tienda"),

]