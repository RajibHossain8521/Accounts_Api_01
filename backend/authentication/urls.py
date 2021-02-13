from django.urls import path

from .views import (
    user_registration_view,
    verify_email_view,
    resend_verify_email_view,
    LoginView,
    LogoutView,
    ResetPasswordEmailView,
    ResetPasswordTokenCheckView,
    SetNewPasswordView,
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('user-registration/', user_registration_view, name='user-registration'),
    path('email-verify/', verify_email_view, name='email-verify'),
    path('resend-verify-email/', resend_verify_email_view, name='resend-verify-email'),
]