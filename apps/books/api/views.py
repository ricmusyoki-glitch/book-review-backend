from rest_framework import generics

from apps.books.models import Book
from .serializers import BookSerializer


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)