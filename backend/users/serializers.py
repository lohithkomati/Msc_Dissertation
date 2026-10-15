from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [

            "id",

            "username",

            "email",

            "first_name",

            "last_name",

            "role",

            "university",

            "programme",

            "year",

            "avatar",

            "bio",

            "consultation_count",

            "average_score",

        ]


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
    )

    class Meta:

        model = User

        fields = [

            "username",

            "email",

            "password",

            "first_name",

            "last_name",

        ]

    def validate_password(self, value):

        validate_password(value)

        return value

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user