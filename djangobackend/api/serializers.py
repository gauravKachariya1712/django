from rest_framework import serializers
from .models import student,employee,commite

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id','stuname','email']

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id','empname','email','dept']

class commiteserializer(serializers.ModelSerializer):
    class Meta:
        model = commite
        fields = ['id','name','email','role']