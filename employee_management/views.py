from rest_framework import viewsets
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Employee ViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Employee modelini yöneten API viewset'i.
    """
    queryset = Employee.objects.all()  # Employee modelini veritabanından alıyoruz
    serializer_class = EmployeeSerializer  # Employee verilerini serialize etmek için
    permission_classes = [IsAuthenticated]  # Sadece giriş yapan kullanıcılar erişebilir

    def create(self, request, *args, **kwargs):
        """
        Yeni bir employee (çalışan) oluşturmak için kullanılan metod.
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Var olan bir employee'yi güncellemek için kullanılan metod.
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Bir employee'yi silmek için kullanılan metod.
        Yalnızca admin kullanıcıları silme işlemi yapabilir.
        """
        if not request.user.is_staff:  # Admin olmayan kullanıcılar silme işlemi yapamaz
            return Response(
                {"detail": "Yalnızca admin kullanıcıları silme işlemi yapabilir."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)


# Department ViewSet
class DepartmentViewSet(viewsets.ModelViewSet):
    """
    Department modelini yöneten API viewset'i.
    """
    queryset = Department.objects.all()  # Department modelini veritabanından alıyoruz
    serializer_class = DepartmentSerializer  # Department verilerini serialize etmek için
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar erişebilir

    # ModelViewSet zaten CRUD işlemlerini sağladığı için aşağıdaki metodu silmeniz gerekmektedir
    # Bu metod gereksizdir çünkü ModelViewSet zaten 'list', 'create', 'retrieve', 'update' ve 'destroy' metodlarına sahiptir.
    # def get_department(request):
    #     from .models import Department  # Yalnızca gerektiği zaman import et
    #     department = Department.objects.all()
    #     return Response(department)          # Bu metodun yerine, ModelViewSet'in sağladığı metodları kullanabilirsiniz.
