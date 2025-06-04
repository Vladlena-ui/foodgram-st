from rest_framework.permissions import BasePermission

class IsSelfOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ('GET', 'HEAD', 'OPTIONS') or obj == request.user
