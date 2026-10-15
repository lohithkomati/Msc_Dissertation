from django.urls import path

from users.views.auth import RegisterView
from users.views.profile import ProfileView
from users.views.password import ChangePasswordView
from users.views.tokens import (
    LoginView,
    RefreshView,
)

urlpatterns = [

    # Authentication
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "refresh/",
        RefreshView.as_view(),
        name="refresh",
    ),

    # User Profile
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile",
    ),

    # Password
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),

]