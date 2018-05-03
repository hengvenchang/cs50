from django.shortcuts import render

# Create your views here.
from book.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
