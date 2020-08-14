from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """
    A simple serializer class to render user data as JSON objects

    Methods
    -------
    create(validated_data)
        overrides the default create method
    """
    class Meta:
        """
        Automatically generates a set of fields based on the User model
        """
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """
        Overrides the default create method to create an authentication token
        when a user is created.
        :param validated_data: the validated username and password
        :return: user
            returns the new user instance
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user