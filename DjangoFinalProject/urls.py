from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employee_management.views import EmployeeViewSet, DepartmentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger API dökümantasyonu ayarları
schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="Employee Management API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@employeeapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

# API router'ı
router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)  # Employee API endpoint
router.register(r'departments', DepartmentViewSet)  # Department API endpoint

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin paneli
    path('api/', include(router.urls)),  # API endpoint'leri
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger Docs
]
