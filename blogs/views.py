from django.core import serializers
from django.views.generic.list import ListView
from django.http import HttpResponse

from .models import Post

class ListPosts(ListView):
	"""
	View to list all posts in the system.
	"""
	model = Post

	def get(self, request):
	    """
	    Return a list of all blogs.
	    """
	    posts = [post for post in Post.objects.all()]
	    return posts


class UserPostLitView(ListPosts):
	"""
	View to list all posts in the system.
	"""
	model = Post

	def get(self, request ,username):
	    """
	    Return a list of all blogs.
	    """

	    user = User.objects.get(username=username)
	    posts = user.posts.all()

	    return posts

