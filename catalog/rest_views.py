from rest_framework import serializers
from rest_framework.response import Response
from .models import Book
from django.shortcuts import render
from rest_framework.decorators import api_view


# Serializes Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'author')

# Invokes client
def client(request):
    return render(request, 'book_client.html')


# Supports get and post methods
@api_view(['GET', 'POST'])
def list_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:  # POST
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Insert into table
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)  # Bad request


# Supports GET, DELETE and PUT methods
@api_view(['GET', 'DELETE', 'PUT'])
def get_book(request, bookid):
    try:
        book = Book.objects.get(id=bookid)
    except:
        return Response(status=404) # Resource not found

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        try:
            book.delete()
            return Response(status=204)  # No content and success
        except:
            return Response(status=500)  # Server error
