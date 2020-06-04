import logging
from django.test import TestCase
from patterns import urls

# TODO add more specific tests for individual endpoints


# class TestPostViews(TestCase):
#   """test case for post views"""
#
#   def test_views(self):
#     """test post views"""
#
#     logging.getLogger().setLevel(logging.DEBUG)
#
#     for route in routes:
#       endpoint = route[0]
#       response = self.client.get('/api/' + endpoint + '/')
#       logging.debug("Testing %s...", endpoint)
#       self.assertEqual(response.status_code, 200)