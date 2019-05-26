#!/usr/bin/python3
# -*- coding: utf-8 -*-
from .models import Employee, Leave
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leave
		fields = '__all__'