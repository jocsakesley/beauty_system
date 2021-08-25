from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
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


class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    services = models.ManyToManyField("Service", related_name="user_employee")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150)
    value = models.FloatField(max_length=6)
    duration = models.DurationField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_user")

    def __str__(self):
        return self.name
