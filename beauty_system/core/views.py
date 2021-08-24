from beauty_system.core.serializers import BusinessSerializer, EmployeeSerializer, ProfessionalSerializer, ServiceSerializer
from beauty_system.core.models import Business, Employee, Professional, Service
from rest_framework.viewsets import ModelViewSet


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        services = Service.objects.filter(user=self.request.user.id)
        return services


