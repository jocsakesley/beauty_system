from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from beauty_system.tenant.models import Client, Domain


class CLientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields ="__all__"


class DomainSerializer(ModelSerializer):
    class Meta:
        model = Domain
        fields ="__all__"

