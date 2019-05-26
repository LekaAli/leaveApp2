# from tastypie.test import ResourceTestCaseMixin
# from django.test import TestCase
#
#
# class APIViewTestCase(ResourceTestCaseMixin, TestCase):
#
#     def test_get_employee(self):
#
#         response = self.api_client.get(uri='/api/employee/get_employee', format='json', data={'emp_number': 'ABLT411'})
#
#     def test_add_new_employee(self):
#
#         response = self.api_client.post(
#             uri='/api/employee/new_employee/',
#             format='json',
#             data={},
#             authentication={'Authorization': 'Bearer %s' % ''}
#         )
#
#     def test_add_new_leave(self):
#
#         response = self.api_client.post(
#             uri='/api/leave/new_leave/',
#             format='json',
#             data={},
#             authentication={'Authorization': 'Bearer %s' % ''}
#         )