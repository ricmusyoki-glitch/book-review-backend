from django.urls import path

from .views import BookCreateView

urlpatterns = [
    path("", BookCreateView.as_view(), name="book-create"),
]
