from rest_framework import generics

from ..entities.Group import Group
from ..serializers.Group import GroupSerializer


class GroupView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all().filter(game=self.kwargs['pk'])


class GroupDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()