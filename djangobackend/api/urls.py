from django.urls import path
from api import views

urlpatterns = [
    path('student/', views.studentList.as_view()),
    path('employee/', views.employeeList.as_view()),
    path('commite/', views.commiteList.as_view()),
]