#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer, LeaveSerializer
from .models import Leave, Employee
from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeViewset(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		request_query_params = self.request.query_params
		results = {'success': False, 'payload': 'Employee Number is Required', 'reason': 'Employee Number is Required'}
		if 'emp_number' in request_query_params:
			try:
				employee = Employee.objects.get(emp_number=request_query_params['emp_number'])
				serializer = EmployeeSerializer(employee)
				results = {'success': True, 'payload': serializer.data}
			except Exception as ex:
				ex = str(ex)
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request):
		results = dict()
		request_query_params = self.request.data
		try:
			employee = Employee.objects.filter(emp_number=request_query_params['emp_number'])
			if employee.count() == 0:
				employee = Employee.objects.create(**request_query_params)
				results.update({'success': True, 'payload': model_to_dict(employee), 'reason': 'Employee Successfully Created'})
			else:
				employee = employee.last()
				employee.first_name = request_query_params['first_name']
				employee.last_name = request_query_params['last_name']
				employee.phone_number = request_query_params['phone_number']
				employee.save()
				results.update({'success': True, 'payload': model_to_dict(employee), 'reason': 'Employee Successfully Updated'})
		except Exception as ex:
			ex = str(ex)
			results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)


class LeaveViewset(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		request_query_params = self.request.query_params
		results = {'success': False, 'payload': 'Employee Number is Required', 'reason': 'Employee Number is Required'}
		if 'emp_number' in request_query_params:
			try:
				employee = Leave.objects.get(employee__emp_number=request_query_params['emp_number'])
				results = {'success': True, 'payload': model_to_dict(employee)}
			except Exception as ex:
				ex = str(ex)
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request, *args, **kwargs):
		request_query_params = self.request.data
		results = dict()
		try:
			emp_number = request_query_params['emp_number']
			employee = Employee.objects.get(emp_number=emp_number)
			pending_leave_request = employee.leave.filter(status=0)
			if pending_leave_request.count() > 0:
				leave = pending_leave_request.last()
				leave.start_date = request_query_params.get('start_date')
				leave.end_date = request_query_params.get('end_date')
				leave.status = request_query_params.get('status')
				leave.save()
				results.update({'success': True, 'payload': model_to_dict(leave), 'reason': 'Leave Request Successfully Updated'})
			else:
				leave_kwargs = {
					'employee': employee,
					'start_date': request_query_params['start_date'],
					'end_date': request_query_params['end_date'],
					'status': 0
				}
				leave = Leave.objects.create(**leave_kwargs)
				results.update({'success': True, 'payload': model_to_dict(leave), 'reason': 'Leave Request Successfully Created'})
		except Exception as ex:
			ex = str(ex)
			results.update({'success': False, 'payload': ex, 'reason': ex})

		return Response(results)
