from rest_framework import serializers
from tracker.models import Device,Coordinate


class DeviceSerializer(serializers.ModelSerializer):
    lat = serializers.SerializerMethodField()
    lon = serializers.SerializerMethodField()
    class Meta:
        model = Device
        exclude =("id",)
    
    def get_lat(self, obj):
        coordinate=None
        try:
            coordinate = Coordinate.objects.filter(device=obj).latest('created_date')
        except Coordinate.DoesNotExist:
            return None
        return coordinate.lat

    def get_lon(self, obj):
        coordinate=None
        try:
            coordinate = Coordinate.objects.filter(device=obj).latest('created_date')
        except Coordinate.DoesNotExist:
            return None
        return coordinate.lon

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = "__all__"
