from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UrlSerializer
from tracker.models import Link
from rest_framework import status
from rest_framework import permissions


class UrlListView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the url items for given requested user
        """
        urls = Link.objects.filter(user=request.user.id)
        serializer = UrlSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Url with given url data
        """
        data = request.data
        data.update({"user": request.user.id})
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlDetailView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, url_id, user_id):
        """
        Helper method to get the object with given url_id, and user_id
        """
        try:
            return Link.objects.get(id=url_id, user=user_id)
        except Link.DoesNotExist:
            return None

    def post(self, request, url_id, *args, **kwargs):
        """
        Updates the todo item with given url_id if exists
        """
        url_instance = self.get_object(url_id, request.user.id)
        if not url_instance:
            return Response(
                {"detail": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = request.data        
        data.update({"user": request.user.id})
        serializer = UrlSerializer(
            instance=url_instance, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, url_id, *args, **kwargs):
        """
        Retrieves the Url with given url_id
        """
        url_instance = self.get_object(url_id, request.user.id)
        if not url_instance:
            return Response(
                {"detail": "Object with url id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UrlSerializer(url_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, url_id, *args, **kwargs):
        """
        Deletes the url item with given url_id if exists
        """
        url_instance = self.get_object(url_id, request.user.id)
        if not url_instance:
            return Response(
                {"detail": "Object with url id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        url_instance.delete()
        return Response(
            {"detail": "Object deleted!"}, status=status.HTTP_200_OK
        )
