from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated

from apps.books.api.serializers import BookSerializer
from apps.books.models import Book
from apps.books.permissions import IsBookOwnerOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "author",
    ]

    search_fields = [
        "title",
        "author",
    ]

    ordering_fields = [
        "title",
        "published_date",
    ]

    ordering = [
        "title",
    ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BookRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = BookSerializer
    permission_classes = [
        IsAuthenticated,
        IsBookOwnerOrReadOnly,
    ]
    queryset = Book.objects.all()