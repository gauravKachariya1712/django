from django.contrib import admin
from .models import employee,commite,student
# Register your models here.

# @admin.register(student)
# @admin.register(employee)
models_list = [student,employee,commite] 
admin.site.register(models_list)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'stuname','email']

class employeeAdmin(admin.ModelAdmin):
    list_display1 = ['id', 'empname','email','dept']
