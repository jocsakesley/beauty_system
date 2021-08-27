from rest_framework import permissions
from beauty_system.core.serializers import BusinessSerializer, EmployeeSerializer, ProfessionalSerializer, ServicePostSerializer, ServiceSerializer
from beauty_system.core.models import Business, Employee, Professional, Service
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProfessionalViewSet(ModelViewSet):
    serializer_class = ProfessionalSerializer

    def get_queryset(self):
        professional= Professional.objects.filter(id=self.request.user.id)
        return professional

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"msg": "Perfil criado com sucesso"}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.id:
            return Response({"msg": "Acesso negado"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().retrieve(request, *args, **kwargs)

class BusinessViewSet(ModelViewSet):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        business = Business.objects.filter(id=self.request.user.id)
        return business

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee = Employee.objects.filter(employee_business__id=self.request.user.id)
        return employee

class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        services = Service.objects.filter(user=self.request.user.id)
        return services
    
    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        data = request.data
        data.update(user=request.user.id)
        serializer = ServicePostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
