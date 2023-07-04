from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwnerOrIsSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_superuser
        )
