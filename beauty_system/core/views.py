from beauty_system.core.serializers import BusinessSerializer, CustomerSerializer, DateTimeSerializer, EmployeeSerializer, ProfessionalSerializer, ScheduleSerializer, ServicePostSerializer, ServiceSerializer
from beauty_system.core.models import Business, Customer, DateTime, Employee, Professional, Schedule, Service
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

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

class AllProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class BusinessViewSet(ModelViewSet):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        business = Business.objects.filter(id=self.request.user.id)
        return business

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"msg": "Perfil criado com sucesso"}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.id:
            return Response({"msg": "Acesso negado"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().retrieve(request, *args, **kwargs)

class AllBusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
 
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee = Employee.objects.filter(employee_business__id=self.request.user.id)
        return employee
    
    @action(detail=True, methods=["GET"])
    def services(self, request, pk):
        services = Service.objects.filter(user_employee__id=pk)
        serializer = ServiceSerializer(data=list(services.values()), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        return Response(serializer.data)

class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.id)
        services = Service.objects.filter(user_employee__employee_business__id=self.request.user.id)
        return services
    

class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class DateTimeViewSet(ModelViewSet):
    queryset = DateTime.objects.all()
    serializer_class = DateTimeSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer