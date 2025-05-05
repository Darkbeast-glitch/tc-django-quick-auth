# tests/test_models.py
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="Testpass123"
    )
    assert user.email == "test@example.com"
    assert user.check_password("Testpass123")
    assert str(user) == "testuser"