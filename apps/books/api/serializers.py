from django.db.models import Avg
from rest_framework import serializers

from apps.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "published_date",
            "created_by",
            "average_rating",
            "review_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by",
            "average_rating",
            "review_count",
            "created_at",
            "updated_at",
        ]

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(
            Avg("rating")
        )["rating__avg"]

        if average is None:
            return None

        return round(average, 2)

    def get_review_count(self, obj):
        return obj.reviews.count()