from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from .models import Book, Library
from .serializers import BookSerializer, LibrarySerializer


# Create your views here.

def basiclayout(request):
    return render(request, 'base.html')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    #permission_classes = [permissions.IsAuthenticated]

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('name')
    serializer_class = LibrarySerializer
    #permission_classes = [permissions.IsAuthenticated]

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Or another permission class as needed

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Or another permission class as needed

class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]  # Or another permission class as needed

class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]  # Or another permission class as needed

def books_list(request):
    query = request.GET.get("q")  # Retrieve the search query from the URL parameters
    books = Book.objects.all()

    if query:
        books = books.filter(name__icontains=query)  # Filter by search query

    # Add pagination
    paginator = Paginator(books, 12)  # Display 12 books per page
    page_number = request.GET.get("page")  # Get the current page number from URL
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'query': query}
    return render(request, 'books_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def libs_list(request):
    libs = Library.objects.all()
    context = {'libs' : libs}
    return render(request, 'libs_list.html', context)

def lib_detail(request, pk):
    lib = get_object_or_404(Library, pk=pk)
    return render(request, 'lib_detail.html', {'lib':lib})

