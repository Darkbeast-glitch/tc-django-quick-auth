# django_quick_auth/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import SignupSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView as SimpleJWTTokenRefreshView
from django.conf import settings

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data['password']

            user = authenticate(request, username=username or email, password=password)
            if user:
                if not getattr(settings, 'QUICK_AUTH', {}).get('USE_JWT', False):
                    login(request, user)

                response_data = {"message": "Login successful"}

                if getattr(settings, 'QUICK_AUTH', {}).get('USE_JWT', False):
                    refresh = RefreshToken.for_user(user)
                    response_data.update({
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    })

                return Response(response_data, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenRefreshView(SimpleJWTTokenRefreshView):
    """
    Refreshes an access token using a valid refresh token.
    """
    pass