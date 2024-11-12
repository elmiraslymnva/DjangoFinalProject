from django.urls import path
from employee_management import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('__debug__/', include('debug_toolbar.urls')),
]
