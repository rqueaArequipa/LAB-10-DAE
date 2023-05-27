from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.Index, name='index'),
    path('tienda/producto/<int:producto_id>/', views.Product, name='producto'),
    path('tienda/category/<int:category_id>/', views.Category, name='category'),
]
