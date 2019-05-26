from django.contrib import admin
from .models import Employee, Leave


class EmployeeModelAdmin(admin.ModelAdmin):

	save_on_top = True
	list_display = ('id', 'emp_number', 'first_name', 'last_name', 'phone_number')


class LeaveModelAdmin(admin.ModelAdmin):

	save_on_top = True
	list_display = ('id', 'employee', 'start_date', 'end_date', 'days_of_leave', 'status')


admin.site.register(Employee, EmployeeModelAdmin)
admin.site.register(Leave, LeaveModelAdmin)