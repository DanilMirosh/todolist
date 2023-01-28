from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated

from todolist.goals.models import Board, BoardParticipant


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user.id


class BoardPermission(IsAuthenticated):

    def has_object_permission(self, request, view, obj: Board):
        _filters: dict = {'user': request.user, 'board': obj}
        if request.method not in permissions.SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**_filters).exists()
