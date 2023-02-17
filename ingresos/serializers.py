from rest_framework import serializers

from .models import CategoriaModel, ProductosModel, IngresoModel, IngresoDetallesModel, ProveedorModel


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


class IngresoSerializer(serializers.ModelSerializer):
    estado = serializers.CharField(required=True)

    class Meta:
        model = IngresoModel
        fields = '__all__'


class IngresoDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = IngresoModel
        fields = ['estado']


class IngresoDetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoDetallesModel
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorModel
        fields = '__all__'


class ProveedorDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = ProveedorModel
        fields = ['estado']
