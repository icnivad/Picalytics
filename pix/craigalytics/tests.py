from models import *
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from django.conf import settings
from django.test import TestCase

#More tests coming soon!

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ViewTest(TestCase):
	def setUp(self):
		self.client=Client()
	
	def test_create_image(self):
		create_view=reverse('create_image')
		self.assertEqual(create_view, '/my_images/')
		resp=self.client.get(create_view)
		self.assertEqual(resp.status_code, 200)