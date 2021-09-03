"""beauty_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from beauty_system.core.views import AllBusinessViewSet, AllProfessionalViewSet, BusinessViewSet, CustomerViewSet, DateTimeViewSet, EmployeeViewSet, ProfessionalViewSet, ScheduleViewSet, ServiceViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'api/v1/professional', ProfessionalViewSet, basename='professional')
router.register(r'api/v1/all_professionals', AllProfessionalViewSet, basename='all_professionals')
router.register(r'api/v1/business', BusinessViewSet, basename="business")
router.register(r'api/v1/all_business', AllBusinessViewSet, basename="all_business")
router.register(r'api/v1/employees', EmployeeViewSet, basename="employees")
router.register(r'api/v1/services', ServiceViewSet, basename='services')
router.register(r'api/v1/schedules', ScheduleViewSet, basename='schedules')
router.register(r'api/v1/datetimes', DateTimeViewSet, basename='datetimes')
router.register(r'api/v1/customers', CustomerViewSet, basename='customers')


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
