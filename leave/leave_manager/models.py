#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


class Employee(models.Model):
	emp_number = models.CharField(max_length=12, blank=False, null=False, unique=True)
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	first_name = models.CharField(max_length=25, blank=True, null=True)
	last_name = models.CharField(max_length=35, blank=True, null=True)

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'

	def __str__(self):
		return self.emp_number


def daysOfLeave(leave_days):
	if leave_days <= 0:
		raise ValidationError('Leave time period is invalid')
	else:
		return leave_days


class Leave(models.Model):
	LEAVE_STATUS = ((0, 'New'), (1, 'Approved'), (2, 'Declined'))
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave', blank=True, null=True)
	start_date = models.DateField()
	end_date = models.DateField()
	days_of_leave = models.SmallIntegerField(blank=True, null=True, validators=[daysOfLeave])
	status = models.SmallIntegerField(choices=LEAVE_STATUS)

	class Meta:
		verbose_name = 'Leave'
		verbose_name_plural = 'Leaves'

	def __str__(self):
		return '%s: %s' % (self.employee.emp_number, self.status)

	@staticmethod
	def process_date(_date):
		from datetime import date

		clean_date = list()
		if isinstance(_date, date):
			clean_date = [_date.year, _date.month, _date.day]
		else:
			_date = _date.split('-')
			for _date_part in _date:
				clean_date.append(int(_date_part))
		return clean_date

	def save(self, *args, **kwargs):
		from datetime import date
		import numpy
		start = date(*self.process_date(self.start_date))
		end = date(*self.process_date(self.end_date))
		self.days_of_leave = numpy.busday_count(start, end)
		super(Leave, self).save(*args, **kwargs)

