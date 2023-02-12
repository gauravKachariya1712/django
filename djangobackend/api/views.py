from django.shortcuts import render
from .serializers import studentserializer,employeeserializer,commiteserializer
from rest_framework.generics import ListAPIView
from .models import student,employee,commite
# Create your views here.

class studentList(ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer

class employeeList(ListAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeserializer

class commiteList(ListAPIView):
    queryset = commite.objects.all()
    serializer_class = commiteserializer
