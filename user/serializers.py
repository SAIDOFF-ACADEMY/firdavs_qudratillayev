
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from .models import User, UserContactApplication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        ref_name = 'AdminUserSerializer'


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContactApplication
        fields = ['full_name', 'phone', 'user']
        ref_name = 'AdminUserContactSerializer'


class UserContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'password',
        )
        ref_name = 'AdminUserCreateSerializer'


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed

        if not user.is_staff:
            raise AuthenticationFailed("Only admins can log in")

        token, _ = Token.objects.get_or_create(user=user)

        return {
            "token": token.key
        }
