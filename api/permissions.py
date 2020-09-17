from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        # Safe methods are allowed (Read only GET methods)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Else return if request user == owner is True/False
        return obj.owner == request.user