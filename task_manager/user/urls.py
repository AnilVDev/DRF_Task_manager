from django.urls import path
from .views import UserRegistrationView, UserLoginView
from  rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
