from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()  #It gets the active user model


class RegisterSerializer(serializers.ModelSerializer):  # This creates a serializer for the model
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User  # these are the fields the registration endpoints accepts
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # it creates a user