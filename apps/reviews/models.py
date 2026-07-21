from django.conf import settings
from django.db import models

from apps.books.models import Book


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "user"],
                name="unique_book_review_per_user",
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"