from django.shortcuts import render
from tienda.models import Categoria, Producto
from rest_framework import viewsets, permissions, filters
from .serializers import CategoriaSerializer, ProductoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.http import HttpResponse

#-----------------------------------ViewSet-----------------------------#
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    #para poder filtrar las categorias
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    #para poder filtrar los productos
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'categoria', 'nombre', 'precio', 'stock')
    search_fields = ('id', 'categoria', 'nombre', 'precio', 'stock')
    

#------------------------------------Vistas Genericas----------------------------------#
class CategoriaViewGeneric(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer
    #para poder filtrar las categorias
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    
    #def list(self, request):
        #queryset = self.get_queryset()
        #serializer = CategoriaSerializer(queryset, many=True)
        #return HttpResponse(serializer.data)
class CategoriaDetailViewGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg  = 'categoria_id'
    serializer_class = CategoriaSerializer
    
class ProductoViewGeneric(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    #para poder filtrar los productos
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'categoria', 'nombre', 'precio', 'stock')
    search_fields = ('id', 'categoria', 'nombre', 'precio', 'stock')
    
class ProductoDetailViewGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    lookup_url_kwarg  = 'producto_id'
    serializer_class = ProductoSerializer
    
    