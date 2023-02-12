from rest_framework import serializers

from productos.models import CategoriaModel, ProductosModel


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class CategoriaNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['nombre']


class DisableCategoriaSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = CategoriaModel
        fields = ['estado']


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['categoria'] = CategoriaNameSerializer(instance.categoria).data

        return response


class ProductosDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = CategoriaModel
        fields = ['estado']
