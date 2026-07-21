from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReviewOwnerOrReadOnly(BasePermission):
    """
    Allow read-only access to authenticated users,
    but only the review owner can update or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user