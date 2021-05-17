"""Proyecto_distribuidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#La declaración de las URL para este proyecto de Django; una "tabla de contenidos" de tu sitio hecho con Django.

from django.urls import path
from base.models import *
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sign_in/', sign_in, name='sign_in'),
    path('implementos/', implements, name='implements'),
    path('pendientes/', pending, name='pending'),
    path('logins/', login, name='login'),
    path('createP/', createPending, name='createPending'),
    path('back/', deletePending, name='deletePending'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
