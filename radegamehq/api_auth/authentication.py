from rest_framework import authentication

from .token import user_from_token, get_header_token


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = get_header_token(request.META)

        user = user_from_token(token)

        return user, None
