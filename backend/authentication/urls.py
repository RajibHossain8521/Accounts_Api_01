from django.urls import path

from .views import (
    UserRegistrationView,
    VerifyEmailView,
    ResendVerifyEmailView,
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
    path('admin/', admin.site.urls),
]
