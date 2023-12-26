from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Player(models.Model):

    nickname = models.CharField(max_length=25, primary_key=True)


class Slot(models.Model):
    lvl = models.OneToOneField("Lvl", on_delete=models.CASCADE)


class Lvl(models.Model):
    exp_required = models.IntegerField(default=50)
    exp_current = models.IntegerField(default=0)
    lvl_current = models.IntegerField(default=0)

    def __str__(self):
        return f"12"


class Party5(models.Model):
    nickname = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="Party5_nick")
    first = models.ForeignKey('Slot', on_delete=models.CASCADE, related_name="first", null=True)
    second = models.ForeignKey('Slot', on_delete=models.CASCADE, related_name="second", null=True)
    third = models.ForeignKey('Slot', on_delete=models.CASCADE, related_name="third", null=True)
    fourth = models.ForeignKey('Slot', on_delete=models.CASCADE, related_name="fourth", null=True)
    fifth = models.ForeignKey('Slot', on_delete=models.CASCADE, related_name="fifth", null=True)

    def __str__(self):
        return f"12"

