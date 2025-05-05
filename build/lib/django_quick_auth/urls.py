# django_quick_auth/urls.py
from django.urls import path
from .views import SignupView, LoginView, TokenRefreshView

app_name = 'django_quick_auth'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  # Fixed from previous response
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]