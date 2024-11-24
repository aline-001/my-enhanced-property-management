from django.urls import path
from .import views



urlpatterns=[
    path("properties/",views.property_list),
    path("units/",views.unit_list),
    path("tenants/",views.tenant_list),
    path("leases/",views.lease_list),
]