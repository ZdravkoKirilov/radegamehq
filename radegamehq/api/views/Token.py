from rest_framework import generics

from ..entities.Token import Token
from ..serializers.Token import TokenSerializer


class TokenView(generics.ListCreateAPIView):
    serializer_class = TokenSerializer

    def get_queryset(self):
        return Token.objects.all().filter(game=self.kwargs['pk'])


class TokenDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TokenSerializer

    def get_queryset(self):
        return Token.objects.all()
