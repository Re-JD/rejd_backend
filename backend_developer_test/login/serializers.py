from .models import User, UserManager
from rest_framework import serializers
from django.contrib.auth import *
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            token = TokenObtainPairSerializer
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': token,
        }

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=255, min_length=8, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, min_length=8, write_only=True
    )
    email = serializers.EmailField(
        max_length=255,
    )
    

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if attrs.get('password', '') == attrs.get('password2', ''):
            password = attrs.get('password', '')
        return attrs
    
    def create(self, validated_data):
        _ = validated_data.pop('password2', 0)
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=5555)
    class Meta:
        model = User
        fields = ['token']