from rest_framework import serializers
from audiobook_api import models


class HelloSerializer(serializers.Serializer):
    name =serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields =('id', 'email', 'name', 'password')

        extra_kwargs  ={
            'password':{
                'write_only': True,
                'style':{'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
        email =validated_data['email'],
        name=validated_data['name'],
        password= validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """Serializes profile feed items"""
#
#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         extra_kwargs = {'user_profile': {'read_only': True}}

class SongItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    name =serializers.CharField(max_length=100)
    class Meta:
        model = models.SongItem
        fields = ('id', 'name', 'duration', 'uploaded_time')
        extra_kwargs = {'user_profile': {'read_only': True}}
class PodcastItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    name =serializers.CharField(max_length=100)
    host =serializers.CharField(max_length=100)
    participants =serializers.CharField(max_length=100)
    class Meta:
        model = models.PodcastItem
        fields = ('id', 'name','host','participants', 'duration', 'uploaded_time')
        extra_kwargs = {'user_profile': {'read_only': True}}

class AudioBookItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    title =serializers.CharField(max_length=100)
    author =serializers.CharField(max_length=100)
    narrator =serializers.CharField(max_length=100)
    class Meta:
        model = models.AudioBookItem
        fields = ('id', 'title','author','narrator', 'duration', 'uploaded_time')
        extra_kwargs = {'user_profile': {'read_only': True}}