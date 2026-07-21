from rest_framework import serializers

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Review
        fields = [
            "id",
            "book",
            "user",
            "rating",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )
        return value

    def validate(self, attrs):
        request = self.context.get("request")
        book = attrs.get("book")

        if request and request.method == "POST" and book:
            if Review.objects.filter(
                book=book,
                user=request.user,
            ).exists():
                raise serializers.ValidationError(
                    "You have already reviewed this book."
                )

        return attrs