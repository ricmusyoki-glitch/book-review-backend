from rest_framework import generics, permissions

from .serializers import RegisterSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.response import Response

from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    """
    Register a new user.
    """

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(TokenObtainPairView):
    """
    Login user and return JWT access and refresh tokens.
    """
    pass


class RefreshTokenView(TokenRefreshView):
    """
    Refresh the access token using a valid refresh token.
    """
    pass

class ProfileView(APIView):
    """
    Return the currently authenticated user's information.
    """

    def get(self, request):
        return Response(
            {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
        )