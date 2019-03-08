from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, permissions, decorators

from .models import AppUser
from .serializers import AppUserSerializer
from .token import create_token


class GetCurrentUserView(RetrieveAPIView):
    serializer_class = AppUserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CreateLocalUserView(CreateAPIView):
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        if 'email' not in request.data or 'password' not in request.data:
            return Response('email and password are required fields', status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        try:
            AppUser.objects.get(email=email)
            return Response('User with that email already exists', status=status.HTTP_400_BAD_REQUEST)
        except AppUser.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            AppUser.objects.create(email=serializer.data['email'], password=serializer.initial_data['password'],
                                   alias=serializer.initial_data['alias'])
            # self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetTokenView(CreateAPIView):
    serializer_class = AppUserSerializer
    permission_classes = []

    @decorators.authentication_classes([])
    @decorators.permission_classes([])
    def create(self, request, *args, **kwargs):
        if 'email' not in request.data or 'password' not in request.data:
            return Response('email and password are required fields', status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']

        try:
            user = AppUser.objects.get(email=email, password=password)
            token = create_token(user)
            return Response({"token": token}, status=status.HTTP_200_OK)
        except AppUser.DoesNotExist:
            return Response({'error': {'message': 'User does not exist'}}, status=status.HTTP_401_UNAUTHORIZED)
