from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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

    # def create(self, validated_data):
    #     email = validated_data['email']
    #     password = validated_data['password']
    #     user = authenticate(email=email, password=password)
    #     try:
    #         if user.is_superuser:
    #             if user is None:
    #                 raise AuthenticationFailed()
    #             try:
    #                 token = Token.objects.get(user=user)
    #             except Token.DoesNotExist:
    #                 token = Token.objects.create(user=user)
    #             return {
    #                 'token': token.key,
    #             }
    #     except AttributeError:
    #         raise AuthenticationFailed()
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if not user:
            raise AuthenticationFailed("Email or password incorrect")

        return {
            'email': user.email,
            'full_name': user.get_full_name,
        }
