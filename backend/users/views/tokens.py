from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class LoginView(TokenObtainPairView):
    """
    JWT Login Endpoint

    POST /api/users/login/

    Request:
    {
        "username": "...",
        "password": "..."
    }

    Response:
    {
        "refresh": "...",
        "access": "..."
    }
    """

    permission_classes = [AllowAny]


class RefreshView(TokenRefreshView):
    """
    JWT Refresh Endpoint

    POST /api/users/refresh/

    Request:
    {
        "refresh": "..."
    }

    Response:
    {
        "access": "..."
    }
    """

    permission_classes = [AllowAny]