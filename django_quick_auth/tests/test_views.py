# tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import override_settings

User = get_user_model()


@pytest.mark.django_db
def test_signup_view():
    client = APIClient()
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "Testpass123",
        "password_confirm": "Testpass123",
    }
    response = client.post(reverse("django_quick_auth:signup"), data)
    assert response.status_code == 201
    assert response.data["message"] == "User created successfully"
    assert User.objects.filter(email="test@example.com").exists()


@pytest.mark.django_db
def test_login_view_session():
    client = APIClient()
    client.csrf_enabled = False  # Disable CSRF for testing
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="Testpass123"
    )
    data = {"email": "test@example.com", "password": "Testpass123"}
    response = client.post(reverse("django_quick_auth:login"), data, format="json")
    assert response.status_code == 200
    assert "sessionid" in response.cookies


@pytest.mark.django_db
@override_settings(QUICK_AUTH={"USE_JWT": True, "LOGIN_FIELD": "email"})
def test_login_view_jwt():
    client = APIClient()
    client.csrf_enabled = False  # Disable CSRF for testing
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="Testpass123"
    )
    data = {"email": "test@example.com", "password": "Testpass123"}
    response = client.post(reverse("django_quick_auth:login"), data, format="json")
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_token_refresh_view():
    client = APIClient()
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="Testpass123"
    )
    refresh = RefreshToken.for_user(user)
    response = client.post(
        reverse("django_quick_auth:token_refresh"), {"refresh": str(refresh)}
    )
    assert response.status_code == 200
    assert "access" in response.data
