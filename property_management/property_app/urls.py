from django.urls import path
from property_app import views
from property_app.views import *

urlpatterns = [
    path('property/', views.property_serializer, name='property-serializer'),
    path('tenant/', tenant_serializer, name='tenant-serializer'),
]
