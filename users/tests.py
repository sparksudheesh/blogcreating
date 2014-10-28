from django.test import TestCase, Client
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class UserTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_index(self):
        user=User.objects.create(username="zzz")
        profile=Profile.objects.create(user=user)

    def test_one(self):
         self.c = Client()
         user=User.objects.create(username="abc")
         profile=Profile.objects.create(user=user)
         self.c.get('/users/1/')
         response = self.c.post('/users/1/', {'user': 'xyz'})
        

        