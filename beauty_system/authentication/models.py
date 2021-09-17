from django.contrib.auth.models import AbstractUser
from django.db import models


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
    
    class Meta:
        verbose_name = "Business"
        verbose_name_plural = "Business"

    def __str__(self):
        return self.name