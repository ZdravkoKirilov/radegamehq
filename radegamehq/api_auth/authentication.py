from rest_framework import authentication
from typing import Tuple

from .token import user_from_token, get_header_token
from .models import AppUser


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request) -> Tuple[AppUser, None]:
        token: str = get_header_token(request)

        user: type(AppUser) = user_from_token(token)
        if user is not None:
            user.is_authenticated = True

        return user, None
