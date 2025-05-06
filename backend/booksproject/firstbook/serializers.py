from rest_framework import serializers
from .models import Book, Library

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [ 'bookid','name', 'author', 'publisher']



class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ['libid','name', 'location']