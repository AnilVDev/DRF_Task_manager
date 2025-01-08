from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserLoginView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
