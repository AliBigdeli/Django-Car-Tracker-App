from rest_framework import serializers
from tracker.models import Link


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
