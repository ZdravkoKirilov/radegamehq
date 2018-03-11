from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import AppUser
from .serializers import AppUserSerializer
from .token import create_token


class CreateLocalUserView(CreateAPIView):
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        if 'email' not in request.POST or 'password' not in request.POST:
            return Response('email and password are required fields', status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        try:
            AppUser.objects.get(email=email)
            return Response('User with that email already exists', status=status.HTTP_400_BAD_REQUEST)
        except AppUser.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetTokenView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        if 'email' not in request.POST or 'password' not in request.POST:
            return Response('email and password are required fields', status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = AppUser.objects.get(email=email, password=password)
            token = create_token(user)
            return Response({"token": token}, status=status.HTTP_200_OK)
        except AppUser.DoesNotExist:
            return Response('User not found', status=status.HTTP_401_UNAUTHORIZED)
