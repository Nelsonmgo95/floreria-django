from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name="productos"),
    path('<slug:categoria_slug>/', views.productos, name='categoria_productos'),
    path('<slug:categoria_slug>/<slug:producto_slug>/', views.detalle_producto, name='detalle_producto'),
]