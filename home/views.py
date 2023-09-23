import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from book.models import Book
from book.serializers import BookSerializer
from django.db.models import Q
from rest_framework import status
from django.core.paginator import Paginator

from .threading import HttpRequestThread

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all().order_by('-id')

    p = Paginator(books, 10)
    page = request.GET.get('page')
    book = p.get_page(page)

    serializer = BookSerializer(book, many=True)
        
    return Response(data=serializer.data)


@api_view(['GET'])
def search_book(request):
    name = request.GET.get('name')
    if name is None or name=="":
        return Response(data={"message":"Kitob nomini kiriting"})
    else:
        books = Book.objects.filter(Q(title__icontains=name) | Q(author__name__icontains=name))

    if not books:
        return Response(data={"message":"Kitob topilmadi"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = BookSerializer(books, many=True)
    return Response(data=serializer.data)



@api_view(['GET'])
def search(request):
    name = request.GET.get('name')
    URL = 'https://konstructor.librarynetbuilder.uz'

    urls = [i['url'] for i in json.loads(requests.get(URL).text)]

    threads = [HttpRequestThread(url=url,name=name) for url in urls]
  
    [t.start() for t in threads]
    [t.join() for t in threads]

    natija = [t.results for t in threads if t.status_code]
   
    return Response(data=natija)



@api_view(['GET'])
def single_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)

    return Response(data=serializer.data)


