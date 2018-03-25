from rest_framework import permissions

SAFE_METHODS1 = ['GET', 'HEAD', 'OPTIONS']
SAFE_METHODS = []


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user and request.user.is_authenticated:
            return True
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated and user.id == obj.owner:
            return True
        else:
            return False
