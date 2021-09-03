from rest_framework import serializers
from beauty_system.core.models import Business, Customer, DateTime, Employee, Schedule, Service, User, Professional

class UserSerializer(serializers.ModelSerializer):
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
        fields = ("id", "name", "email", "password", "cpf", "phone", "address")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "email", "cpf", "phone", "address", "services", "employee_business")


class BusinessSerializer(UserSerializer):
    class Meta:
        model = Business
        fields = ("id", "name", "email", "password", "cnpj", "phone", "address", "employees")


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ("id", "name", "value", "duration")

class ServicePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ("id", "name", "value", "duration", "user_employee")


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("id", "professional", "customer", "services")

class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = ("id", "date", "time", "endtime", "total_value", "schedule")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone", "schedule_customer")
