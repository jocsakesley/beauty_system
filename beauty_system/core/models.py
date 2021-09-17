from beauty_system.authentication.models import Business
import datetime as dt
import time
from datetime import date, datetime
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.db.models import Sum



class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    services = models.ManyToManyField("Service", related_name="employee", blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="employee")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150)
    value = models.FloatField(max_length=6)
    duration = models.DurationField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_user")

    def __str__(self):
        return self.name

class Schedule(models.Model):
   
    professional = models.ForeignKey(Employee, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    customer = models.ForeignKey("Customer", related_name="schedule_customer", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer.name} agendada com {self.professional.name}"

class DateTime(models.Model):

    TIMES = (
       (dt.time(8,0,0), "08:00:00"), 
       (dt.time(8,15,0), "08:15:00"), 
       (dt.time(8,30,0), "08:30:00"), 
       (dt.time(8,45,0), "08:45:00"), 
       (dt.time(9,0,0), "09:00:00"),
       (dt.time(9,15,0), "09:15:00"), 
       (dt.time(9,30,0), "09:30:00"), 
       (dt.time(9,45,0), "09:45:00"),  
    )

    date = models.DateField(default=timezone.now)
    time = models.TimeField(choices=TIMES)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    @property
    def endtime(self):
        endtime = Service.objects.filter(employee=self.schedule.professional).aggregate(Sum("duration"))
        return (datetime.combine(self.date, self.time) + endtime["duration__sum"]).time()

    @property
    def total_value(self):
        total_value = Service.objects.filter(employee=self.schedule.professional).aggregate(Sum("value"))
        return total_value["value__sum"]

class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

