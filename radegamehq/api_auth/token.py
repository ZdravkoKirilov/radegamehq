import jwt
from .models import AppUser


def create_token(user):
    encoded = jwt.encode({'email': user.email, 'password': user.password}, 'secret', algorithm='HS256')
    return encoded


def decode_token(encoded):
    decoded = jwt.decode(encoded, 'secret', algorithms=['HS256'])
    return decoded


def validate_token(token):
    try:
        data = decode_token(token)
    except jwt.exceptions.InvalidTokenError:
        return False
    if 'email' not in data or 'password' not in data:
        return False
    try:
        AppUser.objects.get(email=data['email'], password=data['password'])
        return True
    except AppUser.DoesNotExist:
        return False
