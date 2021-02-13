from rest_framework import serializers

from .models import UserAccounts


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ Validation check for user registration """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserAccounts
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        if len(password) < 6:
            raise serializers.ValidationError({'password': 'Password should be at least 6 characters'})
        return attrs

    def create(self, validated_data):
        return UserAccounts.objects.create_user(**validated_data)


class EmailVerificationSerializer():
    pass


class LoginSerializer():
    pass


class LogoutSerializer():
    pass


class ResetPasswordEmailSerializer():
    pass


class SetNewPasswordSerializer():
    pass
