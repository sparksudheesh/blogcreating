from django.test import TestCase, Client
from blogs.models import Post
from django.contrib.auth.models import User
import json

class BlogTest(TestCase):

    def setUp(self):
        self.c = Client()
 
    def test_index(self):
        user=User.objects.create(username="abc")
        Post.objects.create(title="title1", slug="one", author=user, content="hai hello",public=1, created="2014-10-12 00:00:00", updated="2014-10-12 00:00:00", published="2014-10-12 00:00:00")
        
    def test_one(self):
         self.c = Client()
         user=User.objects.create(username="abc")
         self.c.get('/blogs/1/')
         response = self.c.post('/blogs/1/', {'title': 'title1', 'slug': 'one','author':'user', 'content':'hai hello','public':'1', 'created':'2014-10-12 00:00:00', 'updated':'2014-10-12 00:00:00', 'published':'2014-10-12 00:00:00'})
         #Post.objects.create(title="title1", slug="one", author=user, content="hai hello",public=1, created="2014-10-12 00:00:00", updated="2014-10-12 00:00:00", published="2014-10-12 00:00:00")

        

        

      
        