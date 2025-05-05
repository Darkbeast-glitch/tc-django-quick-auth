# tests/test_serializers.py
import pytest
from django_quick_auth.serializers import SignupSerializer, LoginSerializer
@pytest.mark.django_db
def test_signup_serializer_valid():
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "Testpass123",
        "password_confirm": "Testpass123"
    }
    serializer = SignupSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.check_password("Testpass123")
    
@pytest.mark.django_db
def test_signup_serializer_password_mismatch():
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "Testpass123",
        "password_confirm": "Different123"
    }
    serializer = SignupSerializer(data=data)
    assert not serializer.is_valid()
    assert "password" in serializer.errors

def test_login_serializer_valid():
    data = {
        "email": "test@example.com",
        "password": "Testpass123"
    }
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid()

def test_login_serializer_no_username_or_email():
    data = {
        "password": "Testpass123"
    }
    serializer = LoginSerializer(data=data)
    assert not serializer.is_valid()
    assert "Must provide username or email." in str(serializer.errors)