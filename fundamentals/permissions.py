from rest_framework import permissions


# IsMerchant custom permission class
class IsEmployee(permissions.BasePermission):
    """
    Global permission for only emloyees
    """

    def has_permission(self, request, view):
        return request.user.role == 'employee'
