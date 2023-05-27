from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, CategoriaViewGeneric, CategoriaDetailViewGeneric, ProductoViewGeneric, ProductoDetailViewGeneric
from django.urls import path, include

router = DefaultRouter()

router.register('categoria', CategoriaViewSet, 'categoria')
router.register('producto', ProductoViewSet, 'producto')
urlpatterns = [
    path('',include(router.urls)),
    path('generic/categoria/', CategoriaViewGeneric.as_view(), name='category'),
    path('generic/categoria/<int:categoria_id>/',CategoriaDetailViewGeneric.as_view()),
    path('generic/producto/', ProductoViewGeneric.as_view(), name='category'),
    path('generic/producto/<int:producto_id>/',ProductoDetailViewGeneric.as_view())
]