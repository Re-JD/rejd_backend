from django.urls import path
from . import views
from .views import RegisterView, VerifyEmail
urlpatterns = [
    path('login/', views.login),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
]