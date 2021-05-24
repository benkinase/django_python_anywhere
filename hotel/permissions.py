from rest_framework.permissions import (SAFE_METHODS, IsAuthenticated,
IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions)

#custom permission
class RoomCreatorWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
