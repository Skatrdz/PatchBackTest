from django.contrib.auth.models import Group, User
from rest_framework import serializers
from Api.models import Player, Slot, Party5


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['nickname']


class Party5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Party5
        fields = ["nickname", "first", "second", "third", "fourth", "fifth"]
