from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.books.models import Book
from .serializers import BookSerializer
from apps.books.permissions import IsBookOwnerOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a single book.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsBookOwnerOrReadOnly]