from django.urls import path
from . import views
from .views import RegisterView, VerifyEmail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('login/', views.login),
    path('register/', RegisterView.as_view(), name='register'),
    path('token-verify/',TokenVerifyView.as_view(), name='token_verify'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('test/', views.test),
]
