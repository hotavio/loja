from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('teste2/', views.teste2),
]
