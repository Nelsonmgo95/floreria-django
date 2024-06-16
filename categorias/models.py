from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    imagen_categoria = models.ImageField(upload_to= 'imagenes/categorias', blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def get_url(self):
        return reverse('categoria_productos', args=[self.slug])
    
    def __str__(self):
        return self.nombre_categoria