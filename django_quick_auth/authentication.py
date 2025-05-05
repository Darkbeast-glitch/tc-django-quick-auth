# django_quick_auth/authentication.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that supports login with email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to fetch the user by username first
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                # If username lookup fails, try with email
                user = UserModel.objects.get(email=username)
            except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
                return None

        if user.check_password(password):
            return user
        return None