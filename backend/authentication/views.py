from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.urls import reverse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
import jwt

from .models import UserAccounts
from .serializers import (
    UserRegistrationSerializer,
    EmailVerificationSerializer,
)
from .utils import Util


@api_view(['POST',])
def user_registration_view(request):
    if request.method == 'POST':
        user_info = request.data
        serializer = UserRegistrationSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            
            user_info = serializer.data
            user = UserAccounts.objects.get(email=user_info['email'])
            token = RefreshToken.for_user(user).access_token
            
            current_site = get_current_site(request).domain
            relative_link = reverse('email-verify')
            print(relative_link)
            absurl = 'http://'+current_site+relative_link+"?token="+str(token)
            resend_link = 'http://'+current_site+reverse('resend-verify-email')
            
            email_body = 'Hi '+user.username + ','+ \
                '\n\nUse the link below to verify your email:\n'+ absurl + \
                '\n\nUse the link below to resend verify email\n' + resend_link + \
                '\n\nThank you!'
            data = {'email_body': email_body, 
                    'to_email': user.email, 
                    'email_subject': 'Verify your email'}
            
            Util.send_email(data)
            return Response(
                    {'Response': 'Account created successfully!'},
                    status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET',])
def verify_email_view(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            print(payload)
            user = UserAccounts.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation token expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def resend_verify_email_view(request):
    pass


class ResendVerifyEmailView():
    pass


class LoginView():
    pass


class LogoutView():
    pass


class ResetPasswordEmailView():
    pass


class ResetPasswordTokenCheckView():
    pass


class SetNewPasswordView():
    pass