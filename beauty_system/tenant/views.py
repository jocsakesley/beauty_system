from beauty_system.tenant.serializers import CLientSerializer, DomainSerializer
from beauty_system.tenant.models import Client, Domain
from rest_framework.viewsets import ModelViewSet


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = CLientSerializer

class DomainViewSet(ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer