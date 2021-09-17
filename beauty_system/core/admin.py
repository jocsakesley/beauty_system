from django.contrib import admin
from beauty_system.core.models import Customer, DateTime, Employee, Schedule, Service


admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Customer)
admin.site.register(DateTime)
