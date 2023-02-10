from rest_framework import serializers

from productos.models import CategoriaModel, ProductosModel


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class DisableCategoriaSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = CategoriaModel
        fields = ['estado']


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosModel
        fields = '__all__'


class ProductosDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = CategoriaModel
        fields = ['estado']
