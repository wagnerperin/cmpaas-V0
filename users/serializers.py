from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model   = UserProfile
        fields  = ('url', 'birth_date', 'phone_number', 'gender', 'image', 'owner')
        readonly_fields = ('url', 'image')