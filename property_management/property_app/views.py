from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from property_app.models import Property, Tenant, Units
from property_app.seliarizer import UnitsSerializer, PropertySerializer, TenantSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def units_serializer(request):
    if request.method == 'GET':
        unit=Units.objects.all()
        serializer = UnitsSerializer(unit)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def property_serializer(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tenant_serializer(request):
    if request.method == 'GET':
        tenant = Tenant.objects.all()
        serializer = TenantSerializer(tenant)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
