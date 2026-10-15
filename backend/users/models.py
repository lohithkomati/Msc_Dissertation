from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    STUDENT = "student"
    EDUCATOR = "educator"
    ADMIN = "admin"

    ROLE_CHOICES = [

        (STUDENT, "Student"),

        (EDUCATOR, "Educator"),

        (ADMIN, "Administrator"),

    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=STUDENT,
    )

    university = models.CharField(
        max_length=150,
        blank=True,
    )

    programme = models.CharField(
        max_length=150,
        blank=True,
    )

    year = models.PositiveIntegerField(
        default=1,
    )

    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
    )

    email_verified = models.BooleanField(
        default=False,
    )

    consultation_count = models.PositiveIntegerField(
        default=0,
    )

    average_score = models.FloatField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "-created_at",
        ]

    def __str__(self):

        return self.username