from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import*
from .serializers import PropertySerializer, UnitSerializer, TenantSerializer, LeaseSerializer


@api_view(['GET', 'POST'])
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def property_detail(request, pk):
    try:
        property_instance = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PropertySerializer(property_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        property_instance.delete()
        return Response({'message': 'Property deleted'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def unit_list(request):
    if request.method == 'GET':
        units = Units.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def unit_detail(request, pk):
    if request.method == 'GET':
        unit_instance = Units.objects.get(Units, pk=pk)
        serializer = UnitSerializer(unit_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        unit_instance = Units.objects.filter(Units, pk=pk)
        serializer = UnitSerializer(unit_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unit_instance = Units.objects.filter(Units, pk=pk)
        unit_instance.delete()
        return Response({'message': 'Unit deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tenant_list(request):
        if request.method == 'GET':
            tenants = Tenant.objects.all()
            serializer = TenantSerializer(tenants, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = TenantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tenant_detail(request, pk):
        try:
            tenant_instance = Tenant.objects.get(pk=pk)
        except Tenant.DoesNotExist:
            return Response({'error': 'Tenant not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TenantSerializer(tenant_instance)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TenantSerializer(tenant_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            tenant_instance.delete()
            return Response({'message': 'Tenant deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def lease_list(request):
        if request.method == 'GET':
            leases = Lease.objects.all()
            serializer = LeaseSerializer(leases, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = LeaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def lease_detail(request, pk):
        try:
            lease_instance = Lease.objects.get(pk=pk)
        except Lease.DoesNotExist:
            return Response({'error': 'Lease not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = LeaseSerializer(lease_instance)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = LeaseSerializer(lease_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            lease_instance.delete()
            return Response({'message': 'Lease deleted'}, status=status.HTTP_204_NO_CONTENT)
