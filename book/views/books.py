from rest_framework import generics
from book.models import Book
from book.serializers import BookSerializer
from rest_framework import viewsets

class BooksViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer



    
