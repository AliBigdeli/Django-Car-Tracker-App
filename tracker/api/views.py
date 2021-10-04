from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer, CoordinateSerializer
from tracker.models import Device, Coordinate
from rest_framework import status
from rest_framework import permissions


class DeviceListView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the device items for given requested user
        """
        devices = Device.objects.filter(user=request.user.id)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the device with given url data
        """
        data = request.data
        data.update({"user": request.user.id})
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetailView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, token, user_id):
        """
        Helper method to get the object with given url_id, and user_id
        """
        try:
            return Device.objects.get(token=token, user=user_id)
        except Device.DoesNotExist:
            return None

    def post(self, request, token, *args, **kwargs):
        """
        Updates the device item with given token if exists
        """
        device_instance = self.get_object(token, request.user.id)
        if not device_instance:
            return Response(
                {"detail": "Object with device token does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        data = request.data
        data.update({"user": request.user.id})
        serializer = DeviceSerializer(
            instance=device_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, token, *args, **kwargs):
        """
        Retrieves the Url with given url_id
        """
        device_instance = self.get_object(token, request.user.id)
        if not device_instance:
            return Response(
                {"detail": "Object with url id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = DeviceSerializer(device_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, token, *args, **kwargs):
        """
        Deletes the url item with given url_id if exists
        """
        device_instance = self.get_object(token, request.user.id)
        if not device_instance:
            return Response(
                {"detail": "Object with url id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        device_instance.delete()
        return Response(
            {"detail": "Object deleted!"}, status=status.HTTP_200_OK
        )


class CoordinateListView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_device_obj(self, token, user_id):
        """
        Helper method to get the object with given url_id, and user_id
        """
        try:
            return Device.objects.get(token=token, user=user_id)
        except Device.DoesNotExist:
            return None

    def get(self, request, token, *args, **kwargs):
        """
        List all the coordinate items for given requested user
        """
        device = self.get_device_obj(token,request.user.id)
        coordinates = Coordinate.objects.filter(device=device.id)
        serializer = CoordinateSerializer(coordinates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, token, *args, **kwargs):
        """
        Create the coordinate with given token data
        """
        device_instance = self.get_device_obj(token, request.user.id)
        if not device_instance:
            return Response(
                {"detail": "Object with device token does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        data = request.data
        data.update({"device": device_instance.id})
        serializer = CoordinateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoordinateCurrentView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_device_obj(self, token, user_id):
        """
        Helper method to get the object with given url_id, and user_id
        """
        try:
            return Device.objects.get(token=token, user=user_id)
        except Device.DoesNotExist:
            return None
    def get(self, request,token, *args, **kwargs):
        """
        List all the url items for given requested user
        """
        device_instance = self.get_device_obj(token, request.user.id)
        if not device_instance:
            return Response(
                {"detail": "Object with device token does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        coordinate = Coordinate.objects.filter(device=device_instance.id).latest('created_date')
        serializer = CoordinateSerializer(coordinate, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
