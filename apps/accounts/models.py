from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model.
    Currently behaves exactly like Django's default User.
    Extra fields can be added later.
    """

    pass
