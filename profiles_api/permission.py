from rest_framework import permissions



class UpdateOwnProfile(permissions.BasePermission):
    """Allow iser to edit their oen profil"""
    def has_object_argument(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
