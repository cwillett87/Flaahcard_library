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


class FlashcardList(APIView):

    def get(self, request):
        flashcard = Flashcard.objects.all()
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):

    def get_object(self, collection):
        try:
            return Flashcard.objects.filter(collection=collection)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, collection):
        flashcard = self.get_object(collection)
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def put(self, request, collection):
        flashcard = self.get_object(collection)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, collection):
        flashcard = self.get_object(collection)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlashcardNumber(APIView):

    def get_object(self, pk, word):
        try:
            return Flashcard.objects.get(pk=pk, word=word)
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardSerializer(flashcard)
        return Response(serializer.data)

    def patch(self, request, pk, word):
        flashcard = self.get_object(pk, word=word)
        data = {"card_number": flashcard.card_number + int(1)}
        serializer = FlashcardSerializer(flashcard, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
