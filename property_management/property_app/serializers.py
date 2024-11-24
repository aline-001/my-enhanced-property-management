from rest_framework import serializers
from .models import*


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Units
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class LeaseSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Lease
        fields = '__all__'
