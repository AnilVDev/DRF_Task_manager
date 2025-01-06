from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()  
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirmation']

    def validate(self, attrs):
        """
        Check that passwords match and other validations.
        """
        password = attrs.get('password')
        password_confirmation = attrs.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(_('Passwords do not match.'))

        if len(password) < 8:
            raise serializers.ValidationError(_('Password must be at least 8 characters long.'))

        return attrs

    def create(self, validated_data):
        """
        Create a new user instance with the validated data.
        """
        validated_data.pop('password_confirmation') 
        user = get_user_model().objects.create_user(**validated_data)
        return user



class TokenSerializer(serializers.Serializer):
    refresh_Token = serializers.CharField()

    def validate(self, data):
        try:
            refresh = RefreshToken(data['refresh_Token'])
            access_token = refresh.access_token
            return {'access_token' : str(access_token), 'refresh_token': str(refresh)}
        except Exception as e:
            raise serializers.ValidationError({"refresh_Token": "Invalid refresh token."})

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')

        attrs['user'] = user
        return attrs
