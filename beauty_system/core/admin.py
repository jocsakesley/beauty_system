from django.contrib import admin
from beauty_system.core.models import Business, Customer, DateTime, Employee, Professional, Schedule, Service

admin.site.register(Professional)
admin.site.register(Business)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Customer)
admin.site.register(DateTime)
