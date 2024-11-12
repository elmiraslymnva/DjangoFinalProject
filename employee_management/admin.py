from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'hire_date_display']  # hire_date eklenebilir
    list_filter = ['hire_date']  # Hire date'e göre filtreleme
    search_fields = ['first_name', 'last_name', 'email']  # Ada veya e-postaya göre arama
    date_hierarchy = 'hire_date'  # Hire date ile tarihsel erişim
    fieldsets = (
        ('Kişisel Bilgiler', {'fields': ('first_name', 'last_name', 'email')}),
        ('İş Bilgileri', {'fields': ('hire_date',)}),
    )
    def hire_date_display(self, obj):
        return obj.hire_date if obj.hire_date else "N/A"
    hire_date_display.short_description = 'Hire Date'

admin.site.register(Employee, EmployeeAdmin)
