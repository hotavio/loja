"""livraria URL Configuration

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
from django.contrib import admin
from django.db import router
from django.urls import path, include
from django.urls.conf import include

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'categorias-viewset', views.CategoriaViewSet)
router.register(r'fabricantes-viewset', views.FabricanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('teste2/', views.teste2),
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriasDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
    path('', include(router.urls)),
    path('fabricantes-generic/', views.FabricantesListGeneric.as_view()),
    path('fabricantes-generic/<int:id>/',
         views.FabricanteDetailGeneric.as_view()),
]
