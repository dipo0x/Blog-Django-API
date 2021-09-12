from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'user', 'name', 'age', 'address']

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']