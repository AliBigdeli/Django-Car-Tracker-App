from rest_framework import serializers
from tracker.models import Device,Coordinate


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = "__all__"
