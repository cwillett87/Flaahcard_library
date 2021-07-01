from .models import Collection, Flashcard
from .serializers import CollectionSerializer, FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionDetail(APIView):

    def get_object(self, title):
        try:
            return Collection.objects.get(title=title)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, title):
        collection = self.get_object(title)
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def put(self, request, title):
        collection = self.get_object(title)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, title):
        collection = self.get_object(title)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
