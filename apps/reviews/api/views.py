from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.reviews.models import Review
from apps.reviews.api.serializers import ReviewSerializer
from apps.reviews.permissions import IsReviewOwnerOrReadOnly


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwnerOrReadOnly]
    queryset = Review.objects.all()