from urllib import request
from django.shortcuts import render
from studentportalapp.models import Book
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from studentportalapp.serializer import BookSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def book_list(request):
    books=Book.objects.all() #complex data
    serializer =BookSerializer(books,many=True)
    return Response(serializer.data)

    # books_python=list(books.values())
    # return JsonResponse({
    #     'books':books_python
    # })    
@api_view(['POST'])
def book_create(request):
    serializer =BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors) 

@api_view(['GET', 'PUT', 'DELETE'])
def book(request,pk):
    try:
        book=Book.objects.get(pk=pk)
    except:
        return Response({
            'Error':'Book Does not Exist'
        },status=status.HTTP_404_NOT_FOUND)    
    
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data)

    if request.method=='PUT':
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)    

    if request.method == 'DELETE':
        book.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)