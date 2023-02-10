from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from productos.models import CategoriaModel, ProductosModel
from productos.serializers import CategoriaSerializer, DisableCategoriaSerializer, ProductosSerializer, \
    ProductosDisableSerializer


class CategoriaViewSet(viewsets.ViewSet):

    def list(self, request):
        categoria = CategoriaModel.objects.all()
        serializer = CategoriaSerializer(categoria, many=True, context={'request': request})
        response = {
            'error': False,
            'message': 'Todas las Categorias',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=CategoriaSerializer)
    def create(self, request):
        try:
            serializer = CategoriaSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'detail': 'Guardado Correctamente'}
        except:
            response = {'error': True, 'detail': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=DisableCategoriaSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Categoria')
    def disable_categoria(self, request, pk=None):
        try:
            queryset = CategoriaModel.objects.all()
            categorias = get_object_or_404(queryset, pk=pk)
            serializer = DisableCategoriaSerializer(categorias, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'detail': 'Guardado Correctamente'}
        except:
            response = {'error': False, 'detail': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=CategoriaSerializer)
    def update(self, request, pk=None):
        try:
            queryset = CategoriaModel.objects.all()
            categoria = get_object_or_404(queryset, pk=pk)
            serializer = CategoriaSerializer(categoria, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'details': 'Actualizado correctamente'}

        except:
            response = {'error': True, 'details': serializer.errors}

        return Response(response)


class ProductoViewSet(viewsets.ViewSet):

    def list(self, request):
        producto = ProductosModel.objects.all()
        serializer = ProductosSerializer(producto, many=True, context={'request': request})
        response = {
            'error': False,
            'message': 'Todos los productos',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=ProductosSerializer)
    def create(self, request):
        try:
            serializer = ProductosSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'detail': 'Guardado Correctamente'}
        except:
            response = {'error': True, 'detail': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=ProductosDisableSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Producto')
    def disable_producto(self, request, pk=None):
        try:
            queryset = ProductosModel.objects.all()
            productos = get_object_or_404(queryset, pk=pk)
            serializer = ProductosDisableSerializer(productos, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'detail': 'Guardado Correctamente'}
        except:
            response = {'error': False, 'detail': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=ProductosSerializer)
    def update(self, request, pk=None):
        try:
            queryset = ProductosModel.objects.all()
            productos = get_object_or_404(queryset, pk=pk)
            serializer = ProductosSerializer(productos, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'error': False, 'details': 'Actualizado correctamente'}

        except:
            response = {'error': True, 'details': serializer.errors}

        return Response(response)
