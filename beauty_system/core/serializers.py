from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from beauty_system.core.models import Business, Employee, Service, User, Professional

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_superuser = True
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user

class ProfessionalSerializer(UserSerializer):
    class Meta:
        model = Professional
        fields = ("id", "name", "email", "password", "cpf", "phone", "address", "services")

class BusinessSerializer(UserSerializer):
    class Meta:
        model = Business
        fields = ("id", "name", "email", "password", "cnpj", "phone", "address", "employees")

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "email", "cpf", "phone", "address", "services")

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"