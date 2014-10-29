import unittest
from django.test import TestCase, Client
from users.models import Profile
from django.contrib.auth.models import User
from datetime import datetime
import json

class UserTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_index(self):
        user=User.objects.create(username="zzz")
        response = self.client.get('/users/')
        response = self.client.post('/users/', { 'username': '1'})

    def test_edit(self):
        user=User.objects.create(username="abc")
        response = self.client.get('/users/1/')
        response = self.client.post('/users/1/', { 'username':'2'})
        
        

        
