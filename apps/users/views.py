from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .serializers import LoginSerializer, UserRoleSerializer
from .permissions import IsAdminRole

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserRoleViewSet(ModelViewSet):
    """
    API for admin to create users with username, password, role
    and update only the role.
    """
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAdminRole]
