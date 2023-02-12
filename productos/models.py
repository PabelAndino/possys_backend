from django.db import models


class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    estado = models.BooleanField(default=True)


class ProductosModel(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True, default='')
    nombre = models.CharField(max_length=100, blank=False, null=False)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=400, null=True, blank=True)
    estado = models.BooleanField(default=True)

