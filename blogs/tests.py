import unittest
from django.test import TestCase, Client
from blogs.models import Post
from django.contrib.auth.models import User
from datetime import datetime
import json

class BlogTest(TestCase):

    def setUp(self):
        self.client = Client()
 
    def test_index(self):
        user=User.objects.create(username="abc")
        response = self.client.get('/blogs/')
        response = self.client.post('/blogs/', {'title':'title1','slug': 'one', 'author':'user', 'content':'hai hello','public':'1', 'created': '2014-10-12 00:00:00', 'updated': '2014-10-12 00:00:00', 'published':'2014-10-12 00:00:00'  })
        
    def test_edit(self):
        user=User.objects.create(username="abc")
        response = self.client.get('/blogs/1/')
        response = self.client.post('/blogs/1/', { 'title':'hai','slug':'two','author':'user','content':'hai','public':'1','created':'2014-10-29 00:00:00', 'updated': '2014-10-29 00:00:00', 'published':'2014-10-29 00:00:00'  })
        
        

