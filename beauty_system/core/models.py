import datetime as dt
import time
from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models import Sum
from beauty_system.tenant.models import TenantAwareModel


class User(AbstractUser, TenantAwareModel):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=False)
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["username"]


class Professional(User):
    cpf = models.CharField(max_length=14)

    class Meta:
        verbose_name = "Professional"

    def __str__(self):
        return self.name

class Business(User):
    cnpj = models.CharField(max_length=18)
    employees = models.ManyToManyField("Employee", blank=True, related_name="employee_business")

    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Business"

    def __str__(self):
        return self.name


class Employee(TenantAwareModel):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    services = models.ManyToManyField("Service", related_name="user_employee", blank=True)

    def __str__(self):
        return self.name


class Service(TenantAwareModel):
    name = models.CharField(max_length=150)
    value = models.FloatField(max_length=6)
    duration = models.DurationField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_user")

    def __str__(self):
        return self.name

class Schedule(TenantAwareModel):
   
    professional = models.ForeignKey(Employee, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    customer = models.ForeignKey("Customer", related_name="schedule_customer", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer.name} agendada com {self.professional.name}"

class DateTime(TenantAwareModel):

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
        endtime = Service.objects.filter(user_employee=self.schedule.professional).aggregate(Sum("duration"))
        return (datetime.combine(self.date, self.time) + endtime["duration__sum"]).time()

    @property
    def total_value(self):
        total_value = Service.objects.filter(user_employee=self.schedule.professional).aggregate(Sum("value"))
        return total_value["value__sum"]

class Customer(TenantAwareModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

