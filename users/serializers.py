# from django.forms import widgets
from rest_framework import serializers
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile