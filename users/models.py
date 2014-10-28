from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User)
	# username = models.CharField(max_length=30)
	# password = models.CharField(max_length=30)
	# email = models.CharField(max_length=50)

	def __unicode__(self):
		return self.user.username