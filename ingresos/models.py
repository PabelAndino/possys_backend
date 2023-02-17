import datetime

from django.db import models


class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    estado = models.BooleanField(default=True)


class MonedaModel(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    estado = models.BooleanField(default=True)


class ProductosModel(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True, default='')
    nombre = models.CharField(max_length=100, blank=False, null=False)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=400, null=True, blank=True)
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock = models.IntegerField(null=False, default=0)
    moneda = models.CharField(max_length=50, default='cordobas')
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
    fecha_modifiacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=False, null=False, default='aceptado')
    # 2023-02-17T00:00:00Z


class ProveedorModel(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    correo = models.CharField(max_length=100, blank=True, null=True)
    no_ruc = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=False, null=False, default='aceptado')


# Los ingresos deben de ser o solo en cordobas o solo en dolares
class IngresoModel(models.Model):
    fecha_ingreso = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(ProveedorModel, on_delete=models.DO_NOTHING)
    # usuario
    no_factura = models.CharField(max_length=100, blank=False, null=False)
    moneda = models.CharField(max_length=50, default='cordobas')
    total = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.CharField(max_length=50, blank=False, null=False, default='aceptado')


class IngresoDetallesModel(models.Model):
    ingreso = models.ForeignKey(IngresoModel, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProveedorModel, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(null=False, default=0)
    precio_compra_unidad = models.DecimalField(max_digits=6, decimal_places=2)
    precio_venta_unidad = models.DecimalField(max_digits=6, decimal_places=2)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
