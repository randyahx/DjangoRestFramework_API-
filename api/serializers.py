from rest_framework import serializers
from api.models import Messages
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Assign messages to User"""
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Messages.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'messages']


class MessagesSerializer(serializers.ModelSerializer):
    """Create 'owner' field when user creates a message"""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Messages
        fields = ['id', 'owner', 'message']