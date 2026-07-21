from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBookOwnerOrReadOnly(BasePermission):
    """
    Allow anyone with permission to read books,
    but only the owner can update or delete them.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests
        if request.method in SAFE_METHODS:
            return True

        # Only the creator can modify the book
        return obj.created_by == request.user