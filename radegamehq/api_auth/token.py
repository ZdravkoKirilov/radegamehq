import jwt
from .models import AppUser

def create_token(user):
    encoded = jwt.encode({'email': user.email, 'password': user.password}, 'secret', algorithm='HS256')
    return encoded


def decode_token(encoded):
    decoded = jwt.decode(encoded, 'secret', algorithms=['HS256'])
    return decoded


def user_from_token(token):
    try:
        data = decode_token(token)
    except jwt.exceptions.InvalidTokenError:
        return None
    if 'email' not in data or 'password' not in data:
        return None
    try:
        user = AppUser.objects.get(email=data['email'], password=data['password'])
        return user
    except AppUser.DoesNotExist:
        return None


def get_header_token(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        return request.META.get('HTTP_AUTHORIZATION')[7:]
    return None
