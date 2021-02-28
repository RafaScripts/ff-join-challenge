from rest_framework import serializers

from join_site import models


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Target
        fields = "__all__"