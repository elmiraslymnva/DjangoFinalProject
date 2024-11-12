from rest_framework import serializers
from django.contrib.auth.models import User
from employee_management.models import Employee, Department
from django.contrib.auth import authenticate

# EmployeeSerializer (Çalışan bilgilerini serileştirmek için)
class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()  # 'Department' modeline referans
    
    class Meta:
        model = Employee
        fields = '__all__'

# UserRegisterSerializer (Yeni kullanıcı kaydını serileştirmek için)
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']  # Şifre doğrulama için iki alan

    def validate(self, attrs):
        # Şifrelerin eşleşip eşleşmediğini kontrol et
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Şifreler uyuşmuyor."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # 'password2'yi kayıttan çıkar
        user = User.objects.create_user(**validated_data)  # Kullanıcıyı oluştur
        return user

# UserLoginSerializer (Kullanıcı girişi için)
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Kullanıcıyı doğrulamak için 'authenticate' fonksiyonu
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Geçersiz giriş bilgileri.")
        return data

# DepartmentSerializer (Departmanları serileştirmek için)
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'  # Tüm alanları serileştiriyoruz
