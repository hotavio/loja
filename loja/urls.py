from django.contrib import admin
from django.db import router
from django.urls import path, include
from django.urls.conf import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r"categorias-viewset", views.CategoriaViewSet)
router.register(r"fabricantes-viewset", views.FabricanteViewSet)
router.register(r"produto", views.ProdutoViewSet)
router.register(r"compras", views.CompraViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("teste/", views.teste),
    path("teste2/", views.teste2),
    path("categorias/", views.CategoriaView.as_view()),
    path("categorias/<int:id>/", views.CategoriaView.as_view()),
    path("categorias-apiview/", views.CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriasDetail.as_view()),
    path("categorias-generic/", views.CategoriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()),
    path("", include(router.urls)),
    path("fabricantes-generic/", views.FabricantesListGeneric.as_view()),
    path("fabricantes-generic/<int:id>/", views.FabricanteDetailGeneric.as_view()),
]
