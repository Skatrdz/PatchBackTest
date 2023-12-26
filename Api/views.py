from django.shortcuts import render
from rest_framework import viewsets, permissions

from Api.models import Player, Party5
from Api.serializers import PlayerSerializer, Party5Serializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-nickname')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]


class Party5ViewSet(viewsets.ModelViewSet):
    queryset = Party5.objects.all()
    serializer_class = Party5Serializer
    permission_classes = [permissions.IsAuthenticated]



