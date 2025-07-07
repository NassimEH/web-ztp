from django.urls import path

from user.views import profile_views, custom_auth_views
from user.views.custom_auth_views import CustomLoginView

from allauth.account.views import LoginView, SignupView

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(template_name="user/login.html"),
        name="account_login",
    ),
    path(
        "signup/",
        SignupView.as_view(template_name="user/signup.html"),
        name="account_signup",
    ),
    path(
        "logout/",
        custom_auth_views.CustomLogoutView.as_view(),
        name="account_logout",
    ),
    path("me/", profile_views.ProfileView.as_view(), name="account_profile"),
    path(
        "change_password/",
        profile_views.ChangePasswordView.as_view(),
        name="account_change_password",
    ),
]
