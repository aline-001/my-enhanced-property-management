from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(Units)
